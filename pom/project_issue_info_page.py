from selenium.webdriver.common.by import By
from utilities.webdriver_utilities import WebDriverUtilities


class ProjectIssueInfoPage:
    trackerLbl = (By.CSS_SELECTOR, "#content .inline-block")
    subjectLbl = (By.XPATH, "//div[@class='subject']//child::h3")
    descriptionLbl = (By.CSS_SELECTOR, "#issue_description_wiki p")
    statusLbl = (By.XPATH, "//div[text()='Status:']//following-sibling::div")
    priorityLbl = (By.XPATH, "//div[text()='Priority:']//following-sibling::div")
    startDateLbl = (By.XPATH, "//div[text()='Start date:']//following-sibling::div")
    estimatedTimeLbl = (
        By.XPATH,
        "//div[text()='Estimated time:']//following-sibling::div",
    )

    def __init__(self, d):
        self.driver = d
        self.cmd = WebDriverUtilities(self.driver)

    def get_issue_info(self) -> map[str, str]:
        info = {}
        info["Tracker"] = self.cmd.getText(self.trackerLbl)
        info["Subject"] = self.cmd.getText(self.subjectLbl)
        if self.cmd.isElementFoundWithoutWait(self.descriptionLbl):
            info["Description"] = self.cmd.getText(self.descriptionLbl)
        info["Status"] = self.cmd.getText(self.statusLbl)
        info["Priority"] = self.cmd.getText(self.priorityLbl)
        info["StartDate"] = self.cmd.getText(self.startDateLbl)
        info["EstimatedTime"] = self.cmd.getText(self.estimatedTimeLbl)
        return info
