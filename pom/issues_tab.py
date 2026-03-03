from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utilities.webdriver_utilities import WebDriverUtilities


class IssuesTab:

    newIssueLK = (By.XPATH, "//span[text()='New issue']")

    def __init__(self, d: WebDriver):
        self.driver = d
        self.cmd = WebDriverUtilities(driver=self.driver)

    def open_issue_creation_form(self):
        self.cmd.click(self.newIssueLK)
