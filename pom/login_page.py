from selenium.webdriver.common.by import By 
from utilities.webdriver_utilities import WebDriverUtilities

class LoginPage:
    signinLk = (By.LINK_TEXT,"Sign in")
    usernameTB = (By.ID, "username")
    passwordTB = (By.NAME, "password")
    loginBTN = (By.NAME,"login")

    def __init__(self, driver):
        self.driver = driver
        self.cmd = WebDriverUtilities(self.driver)
    
    def nav_to_login_page(self):
        self.cmd.nav_to_url("http://localhost:3000/")
        self.cmd.click(self.signinLk)

    def login(self, un, pw):
        self.cmd.send_text(self.usernameTB, un)
        self.cmd.send_text(self.passwordTB, pw)
        self.cmd.click(self.loginBTN)
        
