from src.main.models.credentials_bundle import Credentials

import os
import dataclasses
import tempfile
import logging

from python_on_whales import DockerClient, Container

logger = logging.getLogger(__name__)

DOCKER_COMPOSE_PATH = "resources/dashed/compose.yaml"


def start_service(service_name: str, credentials_bundle: Credentials, *args) -> bool:
    tmp_file = tempfile.mktemp(prefix=f"dashed-{service_name}-")
    credentials_dict = dataclasses.asdict(credentials_bundle)

    with open(tmp_file, "w") as file:
        file.writelines([f"{arg}='{credentials_dict.get(arg)}'\n" for arg in args])

    try:
        # Start service as defined in docker compose
        docker = DockerClient(
            compose_files=[DOCKER_COMPOSE_PATH],
            compose_env_file=tmp_file
        )

        running_containers: list[Container] = docker.ps()
        # check if the desired container is already running
        already_running = False
        for container in running_containers:
            if container.name.startswith(f'dashed-{service_name}'):
                already_running = True
                logger.info(f"Service {service_name} is already running..")

        if not already_running:
            logger.info(f"Starting {service_name}..")
            docker.compose.up(
                services=[service_name],
                detach=True,
                wait=True
            )
    except BaseException as e:
        return False
    finally:
        os.remove(tmp_file)
    return True


def stop_services() -> bool:
    try:
        # Stop all services defined in docker compose
        docker = DockerClient(
            compose_files=[DOCKER_COMPOSE_PATH]
        )
        docker.compose.down()
    except BaseException as e:
        return False
    return True
