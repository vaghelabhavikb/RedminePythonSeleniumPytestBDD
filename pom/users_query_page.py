from selenium.webdriver.common.by import By

from utilities.webdriver_utilities import WebDriverUtilities


class UsersQueryPage:
	newUserLK = (By.XPATH, "//a/*[text()='New user']")
	userTable = (By.TAG_NAME, "table")
	
	def __init__(self, d):
		self.driver = d
		self.cmd = WebDriverUtilities(self.driver)

	def openUserCreationForm(self):
		self.cmd.click(self.newUserLK)

	def getUserEntry(self, userEntry):
		tableData = self.cmd.getTableDataMap(self.userTable)
		for map in tableData:
			if map.get("Login") == userEntry:
				return map

		for map in tableData:
			if map.get("Login") == userEntry:
				return map

		return {}
