import os

from models import Credentials
from aws_utils import get_credentials_from_sm
from python_on_whales import DockerClient

import tempfile
import logging
logger = logging.getLogger(__name__)


def setup_postgre():
    # Get credentials from secretsmanager
    logger.info("Fetching postgresql credentials from secretmanager")
    pg_credentials: Credentials = get_credentials_from_sm("dashed/postgresql-admin")

    tmp_file = tempfile.mktemp(prefix="dashed-postgre-env-")
    with open(tmp_file, "w") as file:
        file.writelines([
            f"POSTGRES_USER='{pg_credentials.username}'\n",
            f"POSTGRES_PASSWORD='{pg_credentials.password}'\n"
        ])

    try:
        # Start services defined in docker compose
        docker = DockerClient(
            compose_files=["resources/init_services/compose.yaml"],
            compose_env_file=tmp_file
        )

        logger.info("Starting DB..")
        docker.compose.up(
            services=["db"],
            detach=True
        )
    finally:
        os.remove(tmp_file)


def setup_grafana():
    # Get credentials from secretsmanager
    logger.info("Fetching grafana credentials from secretmanager")
    grafana_credentials: Credentials = get_credentials_from_sm("dashed/grafana-admin")

    # Check what else you need from here:
    # - https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/
    # - https://grafana.com/docs/grafana/latest/datasources/postgres/#database-user-permissions-important
    tmp_file = tempfile.mktemp(prefix="dashed-grafana-env-")
    with open(tmp_file, "w") as file:
        file.writelines([
            f"GRAFANA_USER='{grafana_credentials.username}'\n",
            f"GRAFANA_PASSWORD='{grafana_credentials.password}'\n"
        ])

    try:
        # Start services defined in docker compose
        docker = DockerClient(
            compose_files=["resources/init_services/compose.yaml"],
            compose_env_file=tmp_file
        )

        logger.info("Starting Grafana..")
        docker.compose.up(
            services=["grafana"],
            detach=True
        )
    finally:
        os.remove(tmp_file)
