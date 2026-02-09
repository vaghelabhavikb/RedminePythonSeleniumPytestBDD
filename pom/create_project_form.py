from selenium.webdriver.common.by import By
from utilities.webdriver_utilities import WebDriverUtilities
import allure

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

    def check_project_creation_success(self):
        return self.cmd.is_element_present(self.successAlert)
    
    def create_project_with_optional_fields(self, proj_name, project_creation_data):
        self.cmd.send_text(self.name, project_creation_data[proj_name]["ProjectName"])
        if(project_creation_data[proj_name].get("Description") != None):
            self.cmd.send_text(self.desc, project_creation_data[proj_name]["Description"])
        if(project_creation_data[proj_name].get("MarkPublic") != None):
            if(project_creation_data[proj_name]["MarkPublic"] == "false"):
                self.cmd.click(self.markPublic)
        if(project_creation_data[proj_name].get("SubProjectOf") != None):
            match (project_creation_data[proj_name]["SubProjectOf"]):
                case "DocID":
                    self.cmd.select_by_visible_text(self.subOfProj, "DocID")
                case _:
                    allure.attach("Invalid SubProjectOf:" + project_creation_data[proj_name]["SubProjectOf"], attachment_type=allure.attachment_type.TEXT)
        if(project_creation_data[proj_name].get("Identifier") != None):
            self.cmd.clear(self.identifier)
            self.cmd.send_text(self.identifier, project_creation_data[proj_name]["Identifier"])
        self.cmd.click(self.projCreate)
