from models import Credentials

import json
import boto3
from boto3_type_annotations.secretsmanager import Client


def get_credentials_from_sm(secret_name: str) -> Credentials:
    sm_client: Client = boto3.client("secretsmanager")
    credentials_dict = json.loads(sm_client.get_secret_value(SecretId=secret_name).get("SecretString"))

    return Credentials(credentials_dict.get("username"), credentials_dict.get("password"))
