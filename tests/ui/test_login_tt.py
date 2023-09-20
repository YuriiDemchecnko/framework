import pytest


@pytest.mark.uitt
def test_login_page_exists(thinkingTester_lp):
    thinkingTester_lp.get()
    assert thinkingTester_lp.get_title() == "Contact List App"


@pytest.mark.uitt
def test_login(thinkingTester_lp):
    thinkingTester_lp.get()
    thinkingTester_lp.login()
    thinkingTester_lp.logout()


@pytest.mark.uitt
def test_wrong_credentials(thinkingTester_lp):
    thinkingTester_lp.get()
    thinkingTester_lp.login("wrong@email.com", "wrong_pass")
    assert len(thinkingTester_lp.get_error_message()) > 0
