import pytest


@pytest.mark.ttapi
def test_add_user(thinkingTester_api):
    add_user_respone = thinkingTester_api.add_user(
        {
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.d@fake.com",
            "password": "myPassword",
        }
    )
    assert len(add_user_respone) > 0


@pytest.mark.ttapi
def test_user_profile_exists(thinkingTester_api):
    profile_statuscode = thinkingTester_api.get_user_profile()
    assert profile_statuscode == 200


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


@pytest.mark.ttapi
@pytest.mark.parametrize(
    "first_name, data",
    [
        (
            "Nelly",
            {
                "email": "nj1@real.com",
                "city": "New York",
                "stateProvince": "NY",
                "street1": "34 Washington St.",
            },
        ),
        (
            "Helly",
            {
                "email": "hj2@real.com",
                "city": "San Fernando",
                "stateProvince": "CA",
                "phone": "3333333333",
                "postalCode": "11111",
            },
        ),
    ],
)
def test_update_contact(thinkingTester_api, first_name, data):
    update_contact_statuscode = thinkingTester_api.update_contact(first_name, data)
    assert update_contact_statuscode == 200


@pytest.mark.ttapi
def test_contact_list(thinkingTester_api):
    contact_list_response = thinkingTester_api.get_contact_list()
    assert len(contact_list_response) != 0


@pytest.mark.ttapi
def test_get_contact_data(thinkingTester_api):
    get_contact_data = thinkingTester_api.get_contact("Helly")
    assert get_contact_data != None


@pytest.mark.ttapi
@pytest.mark.parametrize("first_name", [("Nelly",), ("Helly",)])
def test_delete_contact(thinkingTester_api, first_name):
    delete_contact_statuscode = thinkingTester_api.delete_contact(first_name[0])
    assert delete_contact_statuscode == 200


@pytest.mark.ttapi
def test_delete_user(thinkingTester_api):
    thinkingTester_api.login(
        {
            "email": "john.d@fake.com",
            "password": "myPassword",
        }
    )
    delete_user_statuscode = thinkingTester_api.delete_user()
    assert delete_user_statuscode == 200
