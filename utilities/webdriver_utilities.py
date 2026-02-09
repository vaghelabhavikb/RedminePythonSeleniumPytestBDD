from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions


class WebDriverUtilities:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.short_wait = WebDriverWait(self.driver, 5)
        self.u_short_wait = WebDriverWait(self.driver, 1)
        self.wait_for_disablility_attempts = 5
        

    def nav_to_url(self, url):
        self.driver.get(url)

    def click_old(self, by):
        self.wait.until(expected_conditions.element_to_be_clickable(by)).click()

    def click(self, by):
        """Clicks an element and retries if it goes stale or isn't ready."""
        attempts = 5
        for i in range(attempts):
            try:
                # Wait until element is both present AND visible
                element = self.wait.until(
                    expected_conditions.element_to_be_clickable(by)
                )
                element.click()
                return  # Success! Exit the method
            except StaleElementReferenceException as e:
                if i == attempts - 1:  # Last attempt
                    raise e
                print(f"Retrying click on {by} due to {type(e).__name__}...")
                time.sleep(1)  # Short breath for the DOM to settle

    def select_by_visible_text(self, by, value):
        element = self.wait.until(expected_conditions.element_to_be_clickable(by))
        Select(element).select_by_visible_text(value)

    def find_element(self, by):
        return self.wait.until(expected_conditions.presence_of_element_located(by))

    def is_element_present(self, by):
        try:
            self.u_short_wait.until(expected_conditions.presence_of_element_located(by))
            return True
        except Exception:
            return False

    def find_elements(self, by):
        return self.wait.until(expected_conditions.presence_of_all_elements_located(by))

    def clear(self, by):
        self.wait.until(expected_conditions.element_to_be_clickable(by)).clear()

    def send_text(self, by, text):
        self.wait.until(expected_conditions.element_to_be_clickable(by)).send_keys(text)

    def send_KB_text(self, by, text):
        actions = ActionChains(self.driver)
        actions.click(self.wait.until(expected_conditions.element_to_be_clickable(by)))
        for ch in text:
            actions.send_keys(ch)
        actions.perform()

    def get_all_elements(self, by):
        return self.wait.until(expected_conditions.presence_of_all_elements_located(by))

    def get_elements_texts(self, by):
        elements = self.get_all_elements(by)
        return [element.text for element in elements]

    def wait_for_element_to_be_disabled(self, by):
        while self.wait_for_disablility_attempts > 0:
            if self.find_element(by).is_enabled():
                self.wait_for_disablility_attempts -= 1
            else:
                return

    def send_tab_key(self):
        ActionChains(self.driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
