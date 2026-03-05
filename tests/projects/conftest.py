import pytest

from pom.projects_query_page import ProjectsQueryPage
from tests.projects.types import (
    IssuesCreationData,
    ProjectsCreationData,
    SpentTimesCreationData,
)


@pytest.fixture
def projects_query_page(cd):
    return ProjectsQueryPage(cd)


@pytest.fixture
def projects_creation_data() -> ProjectsCreationData:
    return {
        "Vendors": {
            "ProjectName": "Vendors",
            "Description": "Vendors Records",
            "MarkPublic": "true",
            "SubProjectOf": "DocID",
        },
        "Accounts": {
            "ProjectName": "Accounts",
            "Description": "Accounts Records",
            "MarkPublic": "false",
            "Identifier": "acc",
            "SubProjectOf": "DocID1",
        },
    }


@pytest.fixture
def issues_creation_data() -> IssuesCreationData:
    return {
        "Ability to insert DocID in the footer of last page": {
            "Tracker": "Story",
            "Subject": "Ability to insert DocID in the footer of last page",
            "Description": "This feature will provide ability to insert DocID in the footer of last page of the document.\nUser can also add/remove/edit the inserted DocID",
            "Status": "Open",
            "Priority": "Medium",
            "StartDate": "05-03-2026",
        },
        "Ability to insert DocID in the Header of last page": {
            "Tracker": "Story",
            "Subject": "Ability to insert DocID in the Header of last page",
            "Status": "Open",
            "Priority": "Low",
            "EstimatedTime": "5:00",
        },
    }


@pytest.fixture
def spent_times_creation_data() -> SpentTimesCreationData:
    return {
        "11:00": {
            "Issue": "Support Edit Time field for DocID",
            "User": "Bhavik Vaghela",
            "Date": "19-03-2026",
            "Hours": "11:00",
            "Comment": "worked on Edit Time field creation in DocID construct",
            "Activity": "In Dev",
        },
        "1:00": {
            "Issue": "Support Edit Time field for DocID",
            "User": "Bhavik Vaghela",
            "Date": "20-03-2026",
            "Hours": "1:00",
            "Activity": "In Dev",
        },
        "2:00": {
            "Issue": "Support Edit Time field for DocID",
            "User": "Bhavik Vaghela",
            "Date": "21-03-2026",
            "Hours": "2:00",
            "Activity": "Dev Review",
        },
    }
