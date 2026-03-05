from tests.projects.types import SpentTimeCreationData
from utilities.webdriver_utilities import WebDriverUtilities
from selenium.webdriver.common.by import By


class CreateSpentTimeForm:
    issue_selector_sb = (By.ID, "time_entry_issue_id")
    support_edit_time_issue_item = (
        By.XPATH,
        "//div[contains(text(),'Support Edit Time field for DocID')]",
    )
    user_select_dd = (By.ID, "time_entry_user_id")
    hours_tb = (By.ID, "time_entry_hours")
    date_picker = (By.ID, "time_entry_spent_on")
    comment_tb = (By.ID, "time_entry_comments")
    activity_dd = (By.ID, "time_entry_activity_id")

    create_btn = (By.NAME, "commit")

    def __init__(self, d):
        self.driver = d
        self.cmd = WebDriverUtilities(self.driver)

    def post_spent_time(self, data: SpentTimeCreationData):
        self.cmd.send_text(self.issue_selector_sb, data["Issue"])
        self.cmd.click(self.support_edit_time_issue_item)
        self.cmd.select_by_visible_text(self.user_select_dd, data["User"])
        self.cmd.send_text(self.date_picker, data["Date"])
        self.cmd.send_text(self.hours_tb, data["Hours"])
        if "Comment" in data:
            self.cmd.send_text(self.comment_tb, data["Comment"])
        self.cmd.select_by_visible_text(self.activity_dd, data["Activity"])

        self.cmd.click(self.create_btn)
