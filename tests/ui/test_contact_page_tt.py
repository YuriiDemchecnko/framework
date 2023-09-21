import pytest


@pytest.mark.uitt
def test_open_contact(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.open_contact("Garry Jeil")
    thinkingTester_lp.logout()


@pytest.mark.uitt
def test_edit_contact(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.open_contact("Garry Jeil")
    thinkingTester_cp.contact_edit(
        {
            "birthdate": "1973-05-01",
            "phone": "1234567810",
            "city": "Los Angeles",
            "stateProvince": "CA",
        }
    )
    thinkingTester_lp.logout()


@pytest.mark.uitt
def test_add_contact(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.add_contact(
        {
            "firstName": "Larry",
            "lastName": "Doe",
            "birthdate": "1968-10-03",
            "email": "larry.d@fake.com",
            "phone": "1111111111",
            "street1": "42 State St.",
            "street2": "Suite B",
            "city": "Las Vegas",
            "stateProvince": "NV",
            "postalCode": "12345",
            "country": "USA",
        }
    )
    thinkingTester_lp.logout()


@pytest.mark.uitt
def test_delete_contact(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.open_contact("Larry Doe")
    thinkingTester_cp.delete_contact()
    thinkingTester_lp.logout()


@pytest.mark.uitt
def test_return_button_press(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.open_contact("Garry Jeil")
    thinkingTester_cp.return_button_press()
    thinkingTester_lp.logout()


@pytest.mark.uitt
def test_cancel_button_press(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.open_contact("Garry Jeil")
    thinkingTester_cp.contact_edit()
    thinkingTester_cp.cancel_button_press()
    thinkingTester_lp.logout()


@pytest.mark.uitt
@pytest.mark.parametrize(
    "input, data",
    [
        (
            "firstName",
            {
                "lastName": "Doe",
                "email": "jd@fake.com",
            },
        ),
        (
            "lastName",
            {
                "firstName": "John",
                "email": "jd@fake.com",
            },
        ),
        (
            "birthdate",
            {
                "firstName": "John",
                "lastName": "Doe",
                "birthdate": "01-01-1965",
            },
        ),
        (
            "email",
            {
                "firstName": "John",
                "lastName": "Doe",
                "email": "123",
            },
        ),
        (
            "phone",
            {
                "firstName": "John",
                "lastName": "Doe",
                "phone": "123",
            },
        ),
        (
            "postalCode",
            {
                "firstName": "John",
                "lastName": "Doe",
                "postalCode": "12",
            },
        ),
    ],
)
def test_add_contact_invalid_data(
    thinkingTester_lp,
    thinkingTester_cp,
    input,
    data,
):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.add_contact(data)
    assert input in thinkingTester_cp.get_error_message()
    thinkingTester_lp.logout()
