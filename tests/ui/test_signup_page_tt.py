import pytest


@pytest.mark.uitt
def test_signup_button_click(thinkingTester_sp):
    thinkingTester_sp.get()
    thinkingTester_sp.signup_button_press()


@pytest.mark.uitt
def test_cancel_button_click(thinkingTester_sp):
    thinkingTester_sp.get()
    thinkingTester_sp.signup_button_press()
    thinkingTester_sp.cancel_button_press()


@pytest.mark.uitt
@pytest.mark.parametrize(
    "input, data",
    [
        (
            "firstName",
            {
                "lastName": "Doe",
                "email": "jd@fake.com",
                "password": "1234567",
            },
        ),
        (
            "lastName",
            {
                "firstName": "John",
                "email": "jd@fake.com",
                "password": "1234567",
            },
        ),
        (
            "email",
            {
                "firstName": "John",
                "lastName": "Doe",
                "password": "1234567",
            },
        ),
        (
            "password",
            {
                "firstName": "John",
                "lastName": "Doe",
                "email": "jd@fake.com",
            },
        ),
    ],
)
def test_add_user_invalid_data(thinkingTester_sp, input, data):
    thinkingTester_sp.get()
    thinkingTester_sp.signup_button_press()
    thinkingTester_sp.add_user(data)
    assert input in thinkingTester_sp.get_error_message()


@pytest.mark.uitt1
def test_add_user(thinkingTester_sp):
    thinkingTester_sp.get()
    thinkingTester_sp.signup_button_press()
