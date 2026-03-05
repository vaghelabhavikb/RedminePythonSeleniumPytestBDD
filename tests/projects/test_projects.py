from datetime import datetime
from math import exp
import pytest
import pytest_check
from pom.create_spent_time_form import CreateSpentTimeForm
from pom.spent_time_tab import SpentTimeTab
from tests.projects.common_steps import *
from tests.common_steps import *
from pytest_bdd import scenarios, given, step, when, then, parsers
from pom.create_issue_form import CreateIssueForm
from pom.issues_tab import IssuesTab
from pom.create_project_form import CreateProjectForm
from pom.project_issue_info_page import ProjectIssueInfoPage
from pom.project_page import ProjectPage
from pom.projects_query_page import ProjectsQueryPage

from tests.projects.types import (
    IssuesCreationData,
    ProjectsCreationData,
    SpentTimesCreationData,
)

scenarios("../../features/projects.feature")


@pytest.fixture
def project_page(cd):
    return ProjectPage(cd)


@pytest.fixture
def issues_tab(cd):
    return IssuesTab(cd)


@pytest.fixture
def spent_time_tab(cd):
    return SpentTimeTab(cd)


@pytest.fixture
def create_issue_form(cd):
    return CreateIssueForm(cd)


@pytest.fixture
def create_spent_time_form(cd):
    return CreateSpentTimeForm(cd)


@pytest.fixture
def create_project_form(cd):
    return CreateProjectForm(cd)


@pytest.fixture
def project_issue_info_page(cd):
    return ProjectIssueInfoPage(cd)


@when("clicks on New Project link to create the project")
def launch_new_project_form(projects_query_page: ProjectsQueryPage):
    projects_query_page.open_project_creation_form()


@when(parsers.parse("User enters {project_name} and creates the project"))
def user_enters_project_name(create_project_form: CreateProjectForm, project_name):
    create_project_form.create_project(project_name)


@then(parsers.parse("{project_name} should be created successfully"))
def check_project_created_succesfully(
    project_name, create_project_form: CreateProjectForm
):
    pytest_check.is_true(create_project_form.check_project_creation_success())
    act = create_project_form.get_created_proj_name()
    pytest_check.equal(
        project_name,
        act,
        "Project Name comparison. |Exp: " + project_name + "| Act: " + act + "|",
    )


@when(parsers.parse("User creates the {project_name} project with optional fields"))
def create_project_with_optional_fields(
    create_project_form: CreateProjectForm,
    project_name,
    projects_creation_data: ProjectsCreationData,
):
    create_project_form.create_project_with_optional_fields(
        projects_creation_data[project_name]
    )


@given(parsers.parse("User open {project_name} project"))
def open_project(projects_query_page: ProjectsQueryPage, project_name):
    projects_query_page.open_project(project_name)


@given("navigates to issues tab")
def navigate_to_issues_tab(project_page: ProjectPage):
    project_page.nav_to_issues_tab()


@when("user opens create issue form")
def user_opens_create_issue_form(issues_tab: IssuesTab):
    issues_tab.open_issue_creation_form()


@when(parsers.parse("enters {issue} fields values and creates issue"))
def user_enters_issue_fields_values_and_creates_issue(
    create_issue_form: CreateIssueForm, issue, issues_creation_data
):
    create_issue_form.create_issue(issues_creation_data[issue])


@then(parsers.parse("the {issue} info should display correct fields values"))
def the_issue_info_should_display_correct_fields_values(
    project_issue_info_page: ProjectIssueInfoPage,
    issue: str,
    issues_creation_data: IssuesCreationData,
):
    act = project_issue_info_page.get_issue_info(list(issues_creation_data[issue]))
    exp = issues_creation_data[issue]

    for key in exp:
        if key == "StartDate":
            exp_date = datetime.strptime(exp[key], "%d-%m-%Y")
            act_date = datetime.strptime(act[key], "%m/%d/%Y")
            pytest_check.equal(
                act_date,
                exp_date,
                "|Actual: "
                + act_date.strftime("%m/%d/%Y")
                + "|Expected: "
                + exp_date.strftime("%m/%d/%Y"),
            )
        else:
            pytest_check.is_in(
                exp[key], act[key], "|Actual: " + act[key] + "|Expected: " + exp[key]
            )


@given("navigates to spent time tab")
def navigate_to_spent_time_tab(project_page: ProjectPage):
    project_page.nav_to_spent_time_tab()


@when("user opens create spent time form")
def user_opens_create_spent_time_form(spent_time_tab: SpentTimeTab):
    spent_time_tab.launch_spent_time_creation_form()


@when(parsers.parse("enters {time_entry} fields values and creates spent time entry"))
def user_enters_spent_time_fields_values_and_creates_entry(
    create_spent_time_form: CreateSpentTimeForm,
    time_entry,
    spent_times_creation_data: SpentTimesCreationData,
):
    create_spent_time_form.post_spent_time(spent_times_creation_data[time_entry])


@then(parsers.parse("the {time_entry} entry should display correct fields values"))
def the_spent_time_entry_should_display_correct_fields_values(
    spent_time_tab: SpentTimeTab,
    time_entry,
    spent_times_creation_data: SpentTimesCreationData,
):
    act = spent_time_tab.get_time_entry(time_entry)
    exp = spent_times_creation_data[time_entry]

    for key in exp:
        if key == "Date":
            exp_date = datetime.strptime(exp[key], "%d-%m-%Y")
            act_date = datetime.strptime(act[key], "%m/%d/%Y")
            pytest_check.equal(
                act_date,
                exp_date,
                "|Actual: "
                + act_date.strftime("%m/%d/%Y")
                + "|Expected: "
                + exp_date.strftime("%m/%d/%Y"),
            )
        else:
            pytest_check.is_in(
                exp[key], act[key], "|Actual: " + act[key] + "|Expected: " + exp[key]
            )
