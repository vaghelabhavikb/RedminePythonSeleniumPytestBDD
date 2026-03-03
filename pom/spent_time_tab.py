
from utilities.webdriver_utilities import WebDriverUtilities
from selenium.webdriver.common.by import By

class SpentTimeTab:

	logTimeLnk = (By.XPATH,"//span[text()='Log time']")
	spentTimeTable = (By.TAG_NAME,"table")

	def __init__(self, d):
		self.driver = d
		self.cmd = WebDriverUtilities(self.driver)

	def launchSpentTimeCreationForm(self):
		self.cmd.click(self.logTimeLnk)	

	def getTimeEntry(self, timeEntry):
		tableData = self.cmd.getTableDataMap(self.spentTimeTable)
		for map in tableData:
			if map.get("Hours") == timeEntry:
				return map
		
		for map in tableData:
			if(map.get("Hours") == timeEntry):
				return map
		
		return {}