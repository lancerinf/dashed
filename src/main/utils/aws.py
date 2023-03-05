from src.main.models.credentials_bundle import Credentials

import boto3
from boto3_type_annotations.secretsmanager import Client


def get_credentials_from_sm(secret_name: str) -> Credentials:
    sm_client: Client = boto3.client("secretsmanager")
    credentials_json = sm_client.get_secret_value(SecretId=secret_name).get("SecretString")

    return Credentials.from_json(credentials_json)
