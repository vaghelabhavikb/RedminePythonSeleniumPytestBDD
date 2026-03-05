
from utilities.webdriver_utilities import WebDriverUtilities
from selenium.webdriver.common.by import By

class AdminPage:
	usersLK = (By.XPATH,"//a/*[text()='Users']")
	
	def __init__(self, d):
		self.driver = d
		self.cmd = WebDriverUtilities(self.driver)

	def openUsersPage(self):
		self.cmd.click(self.usersLK)
