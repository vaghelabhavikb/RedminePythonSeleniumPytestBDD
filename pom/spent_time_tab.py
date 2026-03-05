from utilities.webdriver_utilities import WebDriverUtilities
from selenium.webdriver.common.by import By


class SpentTimeTab:

    log_time_lk = (By.XPATH, "//span[text()='Log time']")
    spent_time_table = (By.TAG_NAME, "table")

    def __init__(self, d):
        self.driver = d
        self.cmd = WebDriverUtilities(self.driver)

    def launch_spent_time_creation_form(self):
        self.cmd.click(self.log_time_lk)

    def get_time_entry(self, time_entry):
        table_data = self.cmd.get_table_data_map(self.spent_time_table)
        for data in table_data:
            if data["Hours"] == time_entry:
                return data

        return {}
