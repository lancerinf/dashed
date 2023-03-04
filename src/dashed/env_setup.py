import os
import dataclasses
import tempfile
import logging

from python_on_whales import DockerClient, Container

from models import Credentials

logger = logging.getLogger(__name__)


def start_service(service_name: str, credentials_bundle: Credentials, *args):
    tmp_file = tempfile.mktemp(prefix=f"dashed-{service_name}-")
    credentials_dict = dataclasses.asdict(credentials_bundle)

    with open(tmp_file, "w") as file:
        file.writelines([f"{arg}='{credentials_dict.get(arg)}'\n" for arg in args])

    try:
        # Start service as defined in docker compose
        docker = DockerClient(
            compose_files=["resources/init_services/compose.yaml"],
            compose_env_file=tmp_file
        )

        running_containers: list[Container] = docker.ps()
        # check if the desired container is already running
        already_running = False
        for container in running_containers:
            if container.name.startswith(f'init_services-{service_name}'):
                already_running = True
                logger.info(f"Service {service_name} is already running..")

        if not already_running:
            logger.info(f"Starting {service_name}..")
            docker.compose.up(
                services=[service_name],
                detach=True,
                wait=True
            )
    finally:
        os.remove(tmp_file)

# Check what else you need from here:
# - https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/
# - https://grafana.com/docs/grafana/latest/datasources/postgres/#database-user-permissions-important
