import pytest


@pytest.mark.uitt
def test_login(thinkingTester_lp):
    thinkingTester_lp.go_to()
    thinkingTester_lp.login()
    thinkingTester_lp.logout()
