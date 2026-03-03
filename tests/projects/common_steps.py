from pytest_bdd import step

from pom.landing_page import LandingPage


@step("User navigate to projects module")
def nav_to_projects_module(landing_page: LandingPage):
    landing_page.nav_to_projects_page()
