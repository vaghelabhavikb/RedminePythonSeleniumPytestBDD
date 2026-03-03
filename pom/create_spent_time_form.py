
from utilities.webdriver_utilities import WebDriverUtilities
from selenium.webdriver.common.by import By

class CreateSpentTimeForm:
	issueSelector = (By.ID,"time_entry_issue_id")
	supportEditTimeIssue = (By.XPATH,"//div[contains(text(),'Support Edit Time field for DocID')]")
	userSelect = (By.ID,"time_entry_user_id")
	hoursTB = (By.ID,"time_entry_hours")
	datePicker = (By.ID,"time_entry_spent_on")
	commentTB = (By.ID,"time_entry_comments")
	activityDD = (By.ID,"time_entry_activity_id")

	createBtn = (By.NAME,"commit")

	def __init__(self, d):
		self.driver = d
		self.cmd = WebDriverUtilities(self.driver)

	def postSpentTime(self, data):
		self.cmd.send_text(self.issueSelector, data.get("Issue"))
		self.cmd.click(self.supportEditTimeIssue)
		self.cmd.select_by_visible_text(self.userSelect, data.get("User"))
		self.cmd.send_text(self.datePicker, data.get("Date"))
		self.cmd.send_text(self.hoursTB, data.get("Hours"))
		if (data.containsKey("Comment")):
			self.cmd.send_text(self.commentTB, data.get("Comment"))
		self.cmd.select_by_visible_text(self.activityDD, data.get("Activity"))

		self.cmd.click(self.createBtn)
