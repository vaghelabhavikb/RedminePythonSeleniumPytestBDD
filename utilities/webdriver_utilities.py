from gettext import find

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions


class WebDriverUtilities:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.stale_solve_wait = WebDriverWait(
            self.driver, 30, 0.5, (StaleElementReferenceException,)
        )
        self.short_wait = WebDriverWait(self.driver, 5)
        self.u_short_wait = WebDriverWait(self.driver, 1)
        self.wait_for_disablility_attempts = 5

    def nav_to_url(self, url):
        self.driver.get(url)

    def get_text(self, by: By) -> str:
        return self.wait.until(
            expected_conditions.visibility_of_element_located(by)
        ).text

    def click(self, by):
        self.wait.until(expected_conditions.element_to_be_clickable(by)).click()

    def click_considering_stale(self, by):
        self.stale_solve_wait.until(
            lambda d: (
                e := d.find_element(*by),
                e.is_displayed(),
                e.is_enabled(),
                e.click(),  # click happens while we still hold fresh reference
                e,  # return element if you need it later
            )[-1]
        )

        # self.stale_solve_wait.until(d d.find_element(by)).click()

    def select_by_visible_text(self, by: By, value: str) -> None:
        element = self.wait.until(expected_conditions.element_to_be_clickable(by))
        Select(element).select_by_visible_text(value)

    def select_by_value(self, by: By, value: str) -> None:
        element = self.wait.until(expected_conditions.element_to_be_clickable(by))
        Select(element).select_by_value(value)

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

    def send_text(self, by: By, text):
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
