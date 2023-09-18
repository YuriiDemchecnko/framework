import pytest


@pytest.mark.uitt
def test_login(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.login()
    thinkingTester_ui.logout()


@pytest.mark.uitt
def test_open_contact(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.login()
    thinkingTester_ui.open_contact("Garry Jeil")
    thinkingTester_ui.logout()


@pytest.mark.uitt
def test_edit_contact(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.login()
    thinkingTester_ui.open_contact("Garry Jeil")
    thinkingTester_ui.contact_edit(
        {
            "birthdate": "1973-05-01",
            "phone": "1234567810",
            "city": "Los Angeles",
            "stateProvince": "CA",
        }
    )
    thinkingTester_ui.logout()


@pytest.mark.uitt
def test_add_contact(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.login()
    thinkingTester_ui.add_contact(
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
    thinkingTester_ui.logout()


@pytest.mark.uitt
def test_delete_contact(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.login()
    thinkingTester_ui.open_contact("Larry Doe")
    thinkingTester_ui.delete_contact()
    thinkingTester_ui.logout()


@pytest.mark.uitt
def test_return_button_press(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.login()
    thinkingTester_ui.open_contact("Garry Jeil")
    thinkingTester_ui.return_button_press()
    thinkingTester_ui.logout()


@pytest.mark.uitt
def test_cancel_button_press(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.login()
    thinkingTester_ui.open_contact("Garry Jeil")
    thinkingTester_ui.contact_edit()
    thinkingTester_ui.cancel_button_press()
    thinkingTester_ui.logout()
