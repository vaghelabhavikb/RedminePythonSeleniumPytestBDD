from ast import Not
from typing import TypedDict, NotRequired


class ProjectCreationData(TypedDict):
    ProjectName: str
    Description: NotRequired[str | None]
    MarkPublic: NotRequired[str | None]
    SubProjectOf: NotRequired[str | None]
    Identifier: NotRequired[str | None]


class ProjectsCreationData(TypedDict):
    ProjectName: ProjectCreationData


class IssueCreationData(TypedDict):
    Tracker: NotRequired[str | None]
    Subject: str
    Description: NotRequired[str | None]
    Status: NotRequired[str | None]
    Priority: NotRequired[str | None]
    StartDate: NotRequired[str | None]
    EstimatedTime: NotRequired[str | None]


class IssuesCreationData(TypedDict):
    Subject: IssueCreationData


class SpentTimeCreationData(TypedDict):
    Issue: NotRequired[str | None]
    User: NotRequired[str | None]
    Date: NotRequired[str | None]
    Hours: str
    Comment: NotRequired[str | None]
    Activity: str


class SpentTimesCreationData(TypedDict):
    Hours: SpentTimeCreationData
