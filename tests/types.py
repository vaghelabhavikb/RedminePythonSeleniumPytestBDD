from typing import TypedDict, NotRequired


class LoginCredentials(TypedDict):
    username: str
    password: str
    keep_signed_in: NotRequired[bool | None]
