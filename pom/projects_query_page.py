from selenium.webdriver.common.by import By 
from utilities.webdriver_utilities import WebDriverUtilities

class ProjectsQueryPage:

    newProjectLK = (By.XPATH,"//a/span[text()='New project']")

    def __init__(self, driver):
        self.driver = driver
        self.cmd = WebDriverUtilities(self.driver)

    def open_project_creation_form(self):
        self.cmd.click(self.newProjectLK)
