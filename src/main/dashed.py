from src.main.utils.docker_services import start_service
from src.main.utils.aws import get_credentials_from_sm
from src.main.models.credentials_bundle import Credentials

import logging

logging.basicConfig(level=logging.INFO)


def main():
    credentials: Credentials = get_credentials_from_sm('dashed/service-credentials')
    # Initialize local db
    start_service('postgres', credentials, 'POSTGRES_USER', 'POSTGRES_PASSWORD')
    # Initialize local Grafana
    start_service('grafana', credentials, 'GRAFANA_USER', 'GRAFANA_PASSWORD', 'POSTGRES_USER', 'POSTGRES_PASSWORD')
    # Initialize data loaders


if __name__ == '__main__':
    main()
