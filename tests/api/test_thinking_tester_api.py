import pytest


@pytest.mark.ttapi
def test_user_profile_exists(thinkingTester_api):
    profile_statuscode = thinkingTester_api.get_user_profile()
    assert profile_statuscode == 200


@pytest.mark.ttapi
def test_contact_list(thinkingTester_api):
    contact_list_statuscode = thinkingTester_api.get_contact_list()
    assert contact_list_statuscode == 200


@pytest.mark.ttapi
@pytest.mark.parametrize(
    "data",
    [
        (
            {
                "firstName": "Nelly",
                "lastName": "Foe",
                "birthdate": "1987-02-01",
                "email": "nf@fake.com",
                "phone": "1111111111",
                "street1": "4 Main St.",
                "street2": "Apartment D",
                "city": "Nebraska",
                "stateProvince": "NC",
                "postalCode": "12345",
                "country": "USA",
            }
        ),
        (
            {
                "firstName": "Helly",
                "lastName": "Roe",
                "birthdate": "1997-02-01",
                "email": "hr@fake.com",
                "phone": "2222222222",
                "street1": "5 Main St.",
                "street2": "Apartment E",
                "city": "Outer Banks",
                "stateProvince": "SC",
                "postalCode": "54321",
                "country": "USA",
            }
        ),
    ],
)
def test_add_contact(thinkingTester_api, data):
    add_contact_statuscode = thinkingTester_api.add_contact(data)
    assert add_contact_statuscode == 201


# data_to_update = {
#     "email": "dj1@real.com",
#     "city": "New York",
#     "stateProvince": "NY",
#     "street1": "34 Washington St.",
# }
