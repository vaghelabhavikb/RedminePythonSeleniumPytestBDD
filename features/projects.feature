Feature: Verify projects workflow
Verify that different projects related workflows are working fine

Background: Login to application
Given User logins to the application with valid credentials
And User navigate to projects module

Scenario Outline: User creates project with name only field
    When clicks on New Project link to create the project
    And User enters <project name> and creates the project
    Then Project should be created successfully

    Examples:
    |project name|
    |Assets      |
    |Fuel Records|

Scenario Outline: Verify creation of projects with optional fields
    When clicks on New Project link to create the project
    And User creates the <project name> project with optional fields
    Then Project should be created successfully

    Examples:
    |project name|
    |Vendors     |
    |Accounts    |

# Scenario: Verify creation of Vendors project with optional fields
#     When clicks on New Project link to create the project
#     And User creates the Vendors project with optional fields
#     Then Project should be created successfully

# Scenario: Verify creation of Accounts project with optional fields
#     When clicks on New Project link to create the project
#     And User creates the Accounts project with optional fields
#     Then Project should be created successfully

Scenario Outline: Verify that user can create issues within a project
    Given user open "DocID" project
    And navigates to issues tab
    When user opens create issue form
    And enters <issue> fields values and creates issue
    Then the <issue> info should display correct fields values

    Examples:
    |issue|
    |Ability to insert DocID in the footer of last page|
    |Ability to insert DocID in the Header of last page|
