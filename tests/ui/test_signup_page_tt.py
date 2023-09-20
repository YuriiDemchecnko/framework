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
