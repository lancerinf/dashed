from src.main.utils.docker_services import start_service, stop_services
from src.main.utils.aws import get_credentials_from_sm
from src.main.models.credentials_bundle import Credentials
from src.main.datasources.postgres import PostgresInitializer

import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main():
    initialized_services: list[str] = []

    try:
        credentials: Credentials = get_credentials_from_sm('dashed/service-credentials')
        # Initialize local db
        service_db_started = start_service('postgres', credentials, 'POSTGRES_USER', 'POSTGRES_PASSWORD')
        if not service_db_started:
            return
        initialized_services.append('postgres')

        db_initializer = PostgresInitializer(credentials)
        db_initializer.initialize_db()

        # Initialize local Grafana
        service_grafana_started = start_service('grafana', credentials, 'GRAFANA_USER', 'GRAFANA_PASSWORD', 'POSTGRES_USER', 'POSTGRES_PASSWORD')
        if not service_grafana_started:
            return
        initialized_services.append('grafana')
        logging.info(f"Started services: {initialized_services}")

        # Initialize data loaders

        # Mock data loader
        while True:
            logging.info(f"Still alive at: {time.time()}")
            time.sleep(60)

    except KeyboardInterrupt as e:
        logger.info(f"Stopping services: {initialized_services}..")
        stopped_correctly = stop_services()
        if stopped_correctly:
            logger.info('Services stopped correctly')
        else:
            logger.error('Some services did not stop correctly')


if __name__ == '__main__':
    main()
