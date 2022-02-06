from enum import Enum

PERSON_PK = "Person"
TABLE_NAME = "HappyExampleTable"

class PersonColumn(Enum):
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    MIDDLE_INITIAL = 'middle_initial'
