import time
import pytest
from pytest_bdd import scenarios, given, step, when, then, parsers
from pom.login_page import LoginPage
from pom.landing_page import LandingPage
from pom.create_project_form import CreateProjectForm
from pom.projects_query_page import ProjectsQueryPage

scenarios("../features/projects.feature")


@pytest.fixture
def login_page(cd):
    return LoginPage(cd)


@pytest.fixture
def landing_page(cd):
    return LandingPage(cd)


@pytest.fixture
def projects_query_page(cd):
    return ProjectsQueryPage(cd)


@pytest.fixture
def create_project_form_page(cd):
    return CreateProjectForm(cd)


@given("User logins to the application with valid credentials")
def login_to_application(login_page: LoginPage):
    login_page.nav_to_login_page()
    login_page.login("admin", "localadmin")


@given("User navigate to projects module")
def nav_to_projects_module(landing_page: LandingPage):
    landing_page.nav_to_projects_page()


@when("clicks on New Project link to create the project")
def launch_new_project_form(projects_query_page: ProjectsQueryPage):
    projects_query_page.open_project_creation_form()


@when(parsers.parse("User enters {project_name} and creates the project"))
def user_enters_project_name(create_project_form_page: CreateProjectForm, project_name):
    create_project_form_page.create_project(project_name)


@then("project should be created successfully")
def check_project_created_succesfully(create_project_form_page: CreateProjectForm):
    pass
