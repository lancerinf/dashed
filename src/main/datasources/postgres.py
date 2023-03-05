from src.main.models.credentials_bundle import Credentials

import logging

POSTGRES_HOST = "find the correct incantation"
logger = logging.getLogger(__name__)


class PostgresInitializer:
    _credentials: Credentials
    _db_connection: str

    def __init__(self, credentials: Credentials):
        self._credentials = credentials
        # TODO establish db connection

    def initialize_db(self):
        if not self._ro_user_exists():
            self._create_read_only_user()

        if not self._garmin_activities_table_exists():
            self._create_garmin_activities_table()

    def _ro_user_exists(self) -> bool:
        # TODO: check if RO user is already in DB
        return False

    def _create_read_only_user(self):
        logger.info("Creating RO user for Grafana to use")
        # TODO: create RO user

    def _garmin_activities_table_exists(self) -> bool:
        # TODO: check if garmin activities table is already in DB
        return False

    def _create_garmin_activities_table(self):
        logger.info("Creating Garmin Activities table in postgres")
        # TODO: create garmin activities table
