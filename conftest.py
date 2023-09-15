import pytest
from modules.api.clients.github import GitHub
from modules.api.clients.thinkingtester import ThinkingTester
from modules.ui.page_objects.sign_in_tt_page import SignInPage


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Name"
        self.second_name = "Secondname"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()

    yield api


@pytest.fixture
def thinkingTester_api():
    tt_api = ThinkingTester()

    yield tt_api


@pytest.fixture
def thinkingTester_ui():
    tt_ui = SignInPage()

    yield tt_ui

    tt_ui.close()
