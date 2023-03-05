from env_setup import start_service
from aws_utils import get_credentials_from_sm
import logging

logging.basicConfig(level=logging.INFO)


def main():
    credentials = get_credentials_from_sm('dashed/service-credentials')
    # Initialize local db
    start_service('postgres', credentials, 'POSTGRES_USER', 'POSTGRES_PASSWORD')
    # Initialize local Grafana
    start_service('grafana', credentials, 'GRAFANA_USER', 'GRAFANA_PASSWORD', 'POSTGRES_USER', 'POSTGRES_PASSWORD')
    # Initialize data loaders


if __name__ == '__main__':
    main()
