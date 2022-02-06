import boto3
from boto3.dynamodb.conditions import Attr
from boto3.dynamodb.conditions import Key

from personification.constants import TABLE_NAME
from personification.constants import PERSON_PK
from personification.constants import PersonColumn


dynamodb = boto3.resource("dynamodb")

def find_people_with_a_middle_initial(dynamodb_table):
    people_with_a_middle_initial = dynamodb_table.query(
        KeyConditionExpression=Key("PK").eq(PERSON_PK),
        FilterExpression=Attr(PersonColumn.MIDDLE_INITIAL.value).exists(),
    )["Items"]
    if not people_with_a_middle_initial:
        return []
    return people_with_a_middle_initial
