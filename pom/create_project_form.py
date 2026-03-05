from selenium.webdriver.common.by import By
from tests.projects.types import ProjectCreationData
from utilities.webdriver_utilities import WebDriverUtilities
import allure


class CreateProjectForm:
    name_tb = (By.ID, "project_name")
    desc_tb = (By.ID, "project_description")
    identifier_tb = (By.ID, "project_identifier")
    mark_public_cb = (By.ID, "project_is_public")
    sub_of_proj_dd = (By.ID, "project_parent_id")
    proj_create_btn = (By.NAME, "commit")

    success_alert_lbl = (By.ID, "flash_notice")
    created_proj_name = (By.CLASS_NAME, "current-project")

    def __init__(self, driver):
        self.driver = driver
        self.cmd = WebDriverUtilities(self.driver)

    def create_project(self, proj_name):
        self.cmd.send_text(self.name_tb, proj_name)
        self.cmd.click(self.proj_create_btn)
        self.cmd.find_element(self.success_alert_lbl)

    def check_project_creation_success(self):
        return self.cmd.is_element_present(self.success_alert_lbl)

    def create_project_with_optional_fields(
        self, project_creation_data: ProjectCreationData
    ):
        self.cmd.send_text(self.name_tb, project_creation_data["ProjectName"])
        if "Description" in project_creation_data:
            self.cmd.send_text(self.desc_tb, project_creation_data["Description"])
        if "MarkPublic" in project_creation_data:
            if project_creation_data["MarkPublic"] == "false":
                self.cmd.click(self.mark_public_cb)
        if "SubProjectOf" in project_creation_data:
            match (project_creation_data["SubProjectOf"]):
                case "DocID":
                    self.cmd.select_by_visible_text(self.sub_of_proj_dd, "DocID")
                case _:
                    allure.attach(
                        "Invalid SubProjectOf:" + project_creation_data["SubProjectOf"],
                        attachment_type=allure.attachment_type.TEXT,
                    )
        if "Identifier" in project_creation_data:
            self.cmd.clear(self.identifier_tb)
            self.cmd.send_text(self.identifier_tb, project_creation_data["Identifier"])
        self.cmd.click(self.proj_create_btn)

    def get_created_proj_name(self):
        return self.cmd.get_text(self.created_proj_name)
