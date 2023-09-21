import pytest
from modules.api.clients.github import GitHub
from modules.api.clients.thinkingtester import ThinkingTester
from modules.ui.page_objects.base_tt import Base
from modules.ui.page_objects.login_page_tt import LoginPage
from modules.ui.page_objects.contact_page_tt import ContactPage
from modules.ui.page_objects.sign_up_page_tt import SignupPage


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


@pytest.fixture(scope="session")
def browser_session():
    browser = Base()
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def thinkingTester_lp(browser_session):
    tt_login_page = LoginPage(browser_session)
    yield tt_login_page


@pytest.fixture(scope="session")
def thinkingTester_cp(browser_session):
    tt_contact_page = ContactPage(browser_session)
    yield tt_contact_page


@pytest.fixture(scope="session")
def thinkingTester_sp(browser_session):
    tt_signup_page = SignupPage(browser_session)
    yield tt_signup_page
