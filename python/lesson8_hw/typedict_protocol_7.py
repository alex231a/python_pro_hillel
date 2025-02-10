"""Module with hw_7"""

from typing import Optional, Dict
from typing_extensions import TypedDict, Protocol


class User(TypedDict):
    """Class User inherits from TypedDict"""
    id: int
    name: str
    is_admin: bool


class UserDatabase(Protocol):
    """Class UserDatabase inherits from Protocol"""
    def get_user(self, user_id: int) -> Optional[User]:
        """Retrieve a user by their ID."""

    def save_user(self, user: User) -> None:
        """Save a user to the database."""


class InMemoryUserDB:
    """Class InMemoryUserDB should have methods from UserDatabase"""
    def __init__(self) -> None:
        """Initialize an empty user database."""
        self._users: Dict[int, User] = {}

    def get_user(self, user_id: int) -> Optional[User]:
        """Retrieve a user by their ID."""
        return self._users.get(user_id)

    def save_user(self, user: User) -> None:
        """Save a user to the in-memory database."""
        self._users[user["id"]] = user


if __name__ == "__main__":

    db = InMemoryUserDB()
    db.save_user({"id": 1, "name": "Alice", "is_admin": False})
    print(db.get_user(1))
    print(db.get_user(2))
