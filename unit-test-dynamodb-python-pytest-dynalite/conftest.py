import subprocess

import boto3
from pytest import fixture

from personification.constants import TABLE_NAME

DYNALITE_PORT = "4567"


@fixture(scope="session")
def dynamodb_table(request):
    proc = subprocess.Popen(
        ["dynalite", "--port", DYNALITE_PORT, "--createTableMs", "0"]
    )
    dynamodb = boto3.resource(
        "dynamodb",
        endpoint_url=f"http://localhost:{DYNALITE_PORT}",
    )

    request.addfinalizer(lambda: proc.kill())

    # Create the table for the first test run
    try:
        table = dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {"AttributeName": "PK", "KeyType": "HASH"},
                {"AttributeName": "SK", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "PK", "AttributeType": "S"},
                {"AttributeName": "SK", "AttributeType": "S"},
            ],
            BillingMode="PAY_PER_REQUEST",
        )
        yield table
    # Reuse the table in subsequent test runs
    except Exception:
        yield dynamodb.Table(TABLE_NAME)
