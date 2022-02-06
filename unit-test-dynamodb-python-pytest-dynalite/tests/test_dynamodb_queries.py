from personification.constants import PersonColumn
from personification.dynamodb_queries import find_people_with_a_middle_initial

def test_find_people_with_a_middle_initial(dynamodb_table):
    dynamodb_table.put_item(
        Item=dict(
            PK="Person",
            SK="123456",
            first_name="John",
            middle_initial="R",
            last_name="Franey",
        )
    )
    dynamodb_table.put_item(
        Item=dict(
            PK="Person",
            SK="234567",
            first_name="Bilbo",
            last_name="Baggins",
        )
    )
    people_with_a_middle_initial = find_people_with_a_middle_initial(dynamodb_table)
    assert len(people_with_a_middle_initial) == 1
    assert people_with_a_middle_initial[0].get(PersonColumn.MIDDLE_INITIAL.value) == "R"
