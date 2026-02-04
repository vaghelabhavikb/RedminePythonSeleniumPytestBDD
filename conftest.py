import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime
import os


@pytest.fixture(scope="function")
def cd(request):
    options = Options()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }

    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    request.node._driver = driver

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    attach_to_allure: bool = True

    if attach_to_allure:

        """
        Hook to inspect test result and take screenshot on failure.
        Works for pytest-bdd scenarios as well.
        """
        outcome = yield
        rep = outcome.get_result()

        if rep.failed:
            driver = getattr(item, "_driver", None)

            if driver:
                # Attach to Allure
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"{item.name}_failure",
                    attachment_type=allure.attachment_type.PNG
                )
    else:
        outcome = yield
        rep = outcome.get_result()

        if rep.failed:
            driver = getattr(item, "_driver", None)

            if driver:
                os.makedirs("screenshots", exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshots/{item.name}_{timestamp}.png"
                driver.save_screenshot(filename)