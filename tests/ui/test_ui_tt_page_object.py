import pytest


@pytest.mark.uitt
def test_login(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.login()
    thinkingTester_ui.logout()


@pytest.mark.uitt
def test_open_first_contact(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.login()
    thinkingTester_ui.open_contact(1)
    thinkingTester_ui.logout()


@pytest.mark.uitt
def test_edit_first_contact(thinkingTester_ui):
    thinkingTester_ui.go_to()
    thinkingTester_ui.login()
    thinkingTester_ui.open_contact(1)
    thinkingTester_ui.contact_edit(
        "Garry",
        "Jeil",
        "New York",
        "1985-11-01",
        "g.j@mail.com",
    )
    thinkingTester_ui.logout()
