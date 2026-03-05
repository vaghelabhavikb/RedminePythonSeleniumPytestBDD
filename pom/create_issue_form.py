from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.projects.types import IssueCreationData, IssuesCreationData
from utilities.webdriver_utilities import WebDriverUtilities


class CreateIssueForm:
    tracker_select = (By.ID, "issue_tracker_id")
    subject_tb = (By.ID, "issue_subject")
    description_tb = (By.ID, "issue_description")
    status_select = (By.ID, "issue_status_id")
    priority_select = (By.ID, "issue_priority_id")
    start_date_picker = (By.ID, "issue_start_date")
    estimated_time = (By.ID, "issue_estimated_hours")
    save_issue = (By.NAME, "commit")

    def __init__(self, d: WebDriver):
        self.driver = d
        self.cmd = WebDriverUtilities(driver=self.driver)

    def create_issue(self, data: IssueCreationData) -> None:
        for key in data:
            match key:
                case "Tracker":
                    self.cmd.select_by_visible_text(
                        self.tracker_select, data["Tracker"]
                    )
                case "Subject":
                    self.cmd.send_text(self.subject_tb, data["Subject"])
                case "Description":
                    self.cmd.send_text(self.description_tb, data["Description"])
                case "Status":
                    self.cmd.select_by_visible_text(self.status_select, data["Status"])
                case "Priority":
                    self.cmd.select_by_visible_text(
                        self.priority_select, data["Priority"]
                    )
                case "StartDate":
                    self.cmd.send_text(self.start_date_picker, data["StartDate"])
                case "EstimatedTime":
                    self.cmd.send_text(self.estimated_time, data["EstimatedTime"])
                case _:
                    print("Incorrect Issue field in test data json: " + key)
        self.cmd.click(self.save_issue)
