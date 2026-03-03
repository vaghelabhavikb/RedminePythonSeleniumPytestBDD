from selenium.webdriver.common.by import By
from tests.types import LoginCredentials
from utilities.webdriver_utilities import WebDriverUtilities


class LoginPage:

    username_tb = (By.ID, "username")
    password_tb = (By.NAME, "password")
    login_btn = (By.NAME, "login")

    def __init__(self, driver):
        self.driver = driver
        self.cmd = WebDriverUtilities(self.driver)

    def login(self, cred: LoginCredentials):
        self.cmd.nav_to_url("http://localhost:3000/login")
        self.cmd.send_text(self.username_tb, cred["username"])
        self.cmd.send_text(self.password_tb, cred["password"])
        self.cmd.click(self.login_btn)
