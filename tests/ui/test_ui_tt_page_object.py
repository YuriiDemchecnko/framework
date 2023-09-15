# from modules.ui.page_objects.sign_in_tt_page import SignInPage
import pytest


@pytest.mark.uitt
def test_login(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.try_login("d1@example.com", "1234567")
    thinkingTester_ui.logout()


@pytest.mark.uitt
def test_open_first_contact(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.try_login("d1@example.com", "1234567")
    thinkingTester_ui.open_first_contact()
    thinkingTester_ui.logout()


@pytest.mark.uitt
def test_edit_first_contact(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.try_login("d1@example.com", "1234567")
    thinkingTester_ui.open_first_contact()
    thinkingTester_ui.first_contact_edit("John", "Doe", "Nebraska")
    thinkingTester_ui.logout()
