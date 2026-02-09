Feature: Verify projects workflow
Verify that different projects related workflows are working fine

Background: Login to application
Given User logins to the application with valid credentials

Scenario Outline: User creates project with name only field
    Given User navigate to projects module
    When clicks on New Project link to create the project
    And User enters <project name> and creates the project
    Then Project should be created successfully

    Examples:
    |project name|
    |Assets      |
    |Fuel Records|

Scenario: Verify creation of Vendors project with optional fields
    Given User navigate to projects module
    When clicks on New Project link to create the project
    And User creates the Vendors project with optional fields
    Then Project should be created successfully

@IP
Scenario: Verify creation of Accounts project with optional fields
    Given User navigate to projects module
    When clicks on New Project link to create the project
    And User creates the Accounts project with optional fields
    Then Project should be created successfully