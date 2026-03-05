from selenium.webdriver.common.by import By
from utilities.webdriver_utilities import WebDriverUtilities


class CreateUserForm:

    loginTB = (By.ID, "user_login")
    firstNameTB = (By.ID, "user_firstname")
    lastNameTB = (By.ID, "user_lastname")
    emailTB = (By.ID, "user_mail")
    isAdminCB = (By.ID, "user_admin")
    passwordTB = (By.ID, "user_password")
    confirmPasswordTB = (By.ID, "user_password_confirmation")

    submitBTN = (By.NAME, "commit")

    usersLK = (By.XPATH, "//a/*[text()='Users']")

    def __init__(self, d):
        self.driver = d
        self.cmd = WebDriverUtilities(self.driver)

    def createUser(self, data: dict[str, str]) -> None:
        self.cmd.send_text(self.loginTB, data.get("Login"))
        self.cmd.send_text(self.firstNameTB, data.get("First name"))
        self.cmd.send_text(self.lastNameTB, data.get("Last name"))
        self.cmd.send_text(self.emailTB, data.get("Email"))
        if "Administrator" in data and data["Administrator"] == "Yes":
            self.cmd.click(self.isAdminCB)

        self.cmd.send_text(self.passwordTB, data.get("Password"))
        self.cmd.send_text(self.confirmPasswordTB, data.get("Password"))

        self.cmd.click(self.submitBTN)

    def navToUsersQueryPage(self):
        self.cmd.click(self.usersLK)
