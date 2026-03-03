from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utilities.webdriver_utilities import WebDriverUtilities


class CreateIssueForm:
    trackerSelect = (By.ID, "issue_tracker_id")
    subjectTB = (By.ID, "issue_subject")
    descriptionTB = (By.ID, "issue_description")
    statusSelect = (By.ID, "issue_status_id")
    prioritySelect = (By.ID, "issue_priority_id")
    startDatePicker = (By.ID, "issue_start_date")
    estimatedTime = (By.ID, "issue_estimated_hours")
    saveIssue = (By.NAME, "commit")

    def __init__(self, d: WebDriver):
        self.driver = d
        self.cmd = WebDriverUtilities(driver=self.driver)

    def create_issue(self, issue, data) -> None:
        for key in data[issue]:
            match key:
                case "Tracker":
                    self.cmd.select_by_visible_text(
                        self.trackerSelect, data[issue][key]
                    )
                case "Subject":
                    self.cmd.send_text(self.subjectTB, data[issue][key])
                case "Description":
                    self.cmd.send_text(self.descriptionTB, data[issue][key])
                case "Status":
                    self.cmd.select_by_visible_text(self.statusSelect, data[issue][key])
                case "Priority":
                    self.cmd.select_by_value(self.prioritySelect, data[issue][key])
                case "StartDate":
                    self.cmd.send_text(self.startDatePicker, data[issue][key])
                case "EstimatedTime":
                    self.cmd.send_text(self.estimatedTime, data[issue][key])
                case _:
                    print("Incorrect Issue field in test data json: " + key)
        self.cmd.click(self.saveIssue)
