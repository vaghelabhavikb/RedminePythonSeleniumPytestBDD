from re import L

from utilities.webdriver_utilities import WebDriverUtilities
from selenium.webdriver.common.by import By


class ProjectPage:

    issuesLK = (By.LINK_TEXT, "Issues")
    spentTimeLK = (By.LINK_TEXT, "Spent time")

    def __init__(self, driver):
        self.driver = driver
        self.cmd = WebDriverUtilities(self.driver)

    def nav_to_issues_tab(self):
        self.cmd.click(self.issuesLK)

    def navToSpentTimeTab(self):
        self.cmd.click(self.spentTimeLK)
