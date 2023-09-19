import pytest


@pytest.mark.uitt1
def test_login_page_exists(thinkingTester_lp):
    thinkingTester_lp.go_to()
    assert thinkingTester_lp.get_title() == "Contact List App"


@pytest.mark.uitt1
def test_login(thinkingTester_lp):
    thinkingTester_lp.go_to()
    thinkingTester_lp.login()
    thinkingTester_lp.logout()


@pytest.mark.uitt1
def test_wrong_credentials(thinkingTester_lp):
    thinkingTester_lp.go_to()
    thinkingTester_lp.login("wrong@email.com", "wrong_pass")
    assert len(thinkingTester_lp.get_error_message()) > 0
