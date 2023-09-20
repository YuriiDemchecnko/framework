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
def test_add_contact_data_without_firstname(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.add_contact(
        {
            "lastName": "Dow",
            "city": "Los Angeles",
            "stateProvince": "CA",
            "country": "USA",
        }
    )
    assert "firstName" in thinkingTester_cp.get_error_message()
    thinkingTester_lp.logout()


@pytest.mark.uitt
def test_add_contact_data_without_lastname(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.add_contact(
        {
            "firstName": "Garry",
            "country": "USA",
        }
    )
    assert "lastName" in thinkingTester_cp.get_error_message()
    thinkingTester_lp.logout()


@pytest.mark.uitt
def test_invalid_phone_number(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.add_contact(
        {
            "firstName": "Garry",
            "lastName": "Doe",
            "phone": "123",
        }
    )
    assert "phone" in thinkingTester_cp.get_error_message()
    thinkingTester_lp.logout()


@pytest.mark.uitt
def test_invalid_birthdate(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.add_contact(
        {
            "firstName": "Garry",
            "lastName": "Doe",
            "birthdate": "01-01-1965",
        }
    )
    assert "birthdate" in thinkingTester_cp.get_error_message()
    thinkingTester_lp.logout()


@pytest.mark.uitt
def test_invalid_postal_code(thinkingTester_lp, thinkingTester_cp):
    thinkingTester_cp.get()
    thinkingTester_lp.login()
    thinkingTester_cp.add_contact(
        {
            "firstName": "Garry",
            "lastName": "Doe",
            "postalCode": "12",
        }
    )
    assert "postalCode" in thinkingTester_cp.get_error_message()
    thinkingTester_lp.logout()
