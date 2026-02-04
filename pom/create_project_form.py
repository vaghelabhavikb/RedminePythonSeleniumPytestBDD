from selenium.webdriver.common.by import By
from utilities.webdriver_utilities import WebDriverUtilities

class CreateProjectForm:
    name = (By.ID, "project_name")
    desc = (By.ID, "project_description")
    identifier = (By.ID, "project_identifier")
    markPublic = (By.ID, "project_is_public")
    subOfProj = (By.ID, "project_parent_id")
    projCreate = (By.NAME, "commit")
    successAlert = (By.ID, "flash_notice")

    def __init__(self, driver):
        self.driver = driver
        self.cmd = WebDriverUtilities(self.driver)

    def create_project(self, proj_name):
        self.cmd.send_text(self.name, proj_name)
        self.cmd.click(self.projCreate)
        self.cmd.find_element(self.successAlert)