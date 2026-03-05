from re import L

from utilities.webdriver_utilities import WebDriverUtilities
from selenium.webdriver.common.by import By


class ProjectPage:

    issues_lk = (By.LINK_TEXT, "Issues")
    spent_time_lk = (By.LINK_TEXT, "Spent time")

    def __init__(self, driver):
        self.driver = driver
        self.cmd = WebDriverUtilities(self.driver)

    def nav_to_issues_tab(self):
        self.cmd.click(self.issues_lk)

    def nav_to_spent_time_tab(self):
        self.cmd.click(self.spent_time_lk)
