import boto3
import os

DB_TABLE = os.getenv("DB_TABLE", "Employee")

def get_dynamodb_table():
    return boto3.resource(
        "dynamodb", region_name="eu-central-1", endpoint_url="http://localhost:8000"
    ).Table(DB_TABLE)
