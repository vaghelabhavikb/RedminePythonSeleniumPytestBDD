from pytest_bdd import given

from pom.login_page import LoginPage
from tests.types import LoginCredentials


@given("User logins to the application with valid credentials")
def login_to_application(login_page: LoginPage, login_credentials: LoginCredentials):
    login_page.login(login_credentials)
