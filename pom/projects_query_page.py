import allure
from selenium.webdriver.common.by import By
from utilities.webdriver_utilities import WebDriverUtilities


class ProjectsQueryPage:

    new_project_link = (By.XPATH, "//a/span[text()='New project']")
    docid_proj_link = (By.LINK_TEXT, "DocID")

    def __init__(self, driver):
        self.driver = driver
        self.cmd = WebDriverUtilities(self.driver)

    def open_project_creation_form(self):
        self.cmd.click(self.new_project_link)

    def open_project(self, proj_name):
        match proj_name:
            case "DocID":
                self.cmd.click(self.docid_proj_link)
            case _:
                allure.attach(
                    "Invalid Project Name: " + proj_name,
                    attachment_type=allure.attachment_type.TEXT,
                )
