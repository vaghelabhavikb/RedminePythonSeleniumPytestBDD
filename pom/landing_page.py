from selenium.webdriver.common.by import By
from utilities.webdriver_utilities import WebDriverUtilities

class LandingPage:
    projectsLK = (By.LINK_TEXT, "Projects")

    def __init__(self, driver):
        self.driver = driver
        self.cmd = WebDriverUtilities(self.driver)

    def nav_to_projects_page(self):
        self.cmd.click(self.projectsLK)
