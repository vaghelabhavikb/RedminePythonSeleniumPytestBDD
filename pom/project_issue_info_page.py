from selenium.webdriver.common.by import By
from tests.projects.types import IssueCreationData
from utilities.webdriver_utilities import WebDriverUtilities


class ProjectIssueInfoPage:
    tracker_lbl = (By.CSS_SELECTOR, "#content .inline-block")
    subject_lbl = (By.XPATH, "//div[@class='subject']//child::h3")
    description_lbl = (By.CSS_SELECTOR, "#issue_description_wiki p")
    status_lbl = (By.XPATH, "//div[text()='Status:']//following-sibling::div")
    priority_lbl = (By.XPATH, "//div[text()='Priority:']//following-sibling::div")
    start_date_lbl = (By.XPATH, "//div[text()='Start date:']//following-sibling::div")
    estimated_time_lbl = (
        By.XPATH,
        "//div[text()='Estimated time:']//following-sibling::div",
    )

    def __init__(self, d):
        self.driver = d
        self.cmd = WebDriverUtilities(self.driver)

    def get_issue_info(self, issue_keys: list) -> IssueCreationData:
        issue_info = IssueCreationData()
        issue_info["Tracker"] = self.cmd.get_text(self.tracker_lbl)
        issue_info["Subject"] = self.cmd.get_text(self.subject_lbl)
        if "Description" in issue_keys:
            issue_info["Description"] = self.cmd.get_text(self.description_lbl)
        issue_info["Status"] = self.cmd.get_text(self.status_lbl)
        issue_info["Priority"] = self.cmd.get_text(self.priority_lbl)
        if "StartDate" in issue_keys:
            issue_info["StartDate"] = self.cmd.get_text(self.start_date_lbl)
        if "EstimatedTime" in issue_keys:
            issue_info["EstimatedTime"] = self.cmd.get_text(self.estimated_time_lbl)
        return issue_info
