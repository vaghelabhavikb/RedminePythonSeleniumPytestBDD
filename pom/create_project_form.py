from selenium.webdriver.common.by import By
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

    def __init__(self, driver):
        self.driver = driver
        self.cmd = WebDriverUtilities(self.driver)

    def create_project(self, proj_name):
        self.cmd.send_text(self.name_tb, proj_name)
        self.cmd.click(self.proj_create_btn)
        self.cmd.find_element(self.success_alert_lbl)

    def check_project_creation_success(self):
        return self.cmd.is_element_present(self.success_alert_lbl)

    def create_project_with_optional_fields(self, proj_name, project_creation_data):
        self.cmd.send_text(
            self.name_tb, project_creation_data[proj_name]["ProjectName"]
        )
        if project_creation_data[proj_name].get("Description") != None:
            self.cmd.send_text(
                self.desc_tb, project_creation_data[proj_name]["Description"]
            )
        if project_creation_data[proj_name].get("MarkPublic") != None:
            if project_creation_data[proj_name]["MarkPublic"] == "false":
                self.cmd.click(self.mark_public_cb)
        if project_creation_data[proj_name].get("SubProjectOf") != None:
            match (project_creation_data[proj_name]["SubProjectOf"]):
                case "DocID":
                    self.cmd.select_by_visible_text(self.sub_of_proj_dd, "DocID")
                case _:
                    allure.attach(
                        "Invalid SubProjectOf:"
                        + project_creation_data[proj_name]["SubProjectOf"],
                        attachment_type=allure.attachment_type.TEXT,
                    )
        if project_creation_data[proj_name].get("Identifier") != None:
            self.cmd.clear(self.identifier_tb)
            self.cmd.send_text(
                self.identifier_tb, project_creation_data[proj_name]["Identifier"]
            )
        self.cmd.click(self.proj_create_btn)
