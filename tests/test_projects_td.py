import pytest

@pytest.fixture
def project_creation_data():
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
