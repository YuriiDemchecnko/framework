import pytest
from modules.api.clients.thinkingtester import ThinkingTester


@pytest.mark.ttapi
def test_user_exists(thinkingTester_api):
    user = thinkingTester_api.get_user_profile()
    assert user["email"] == "d1@example.com"
