import pytest
from pom.landing_page import LandingPage
from pom.login_page import LoginPage
from tests.types import LoginCredentials


@pytest.fixture
def login_credentials() -> LoginCredentials:
    return {"username": "admin", "password": "localadmin"}


# comment added
@pytest.fixture
def login_page(cd):
    return LoginPage(cd)


@pytest.fixture
def landing_page(cd):
    return LandingPage(cd)
