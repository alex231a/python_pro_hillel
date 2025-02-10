"""Module docstring"""
from typing import List, TypeVar, Callable
from typing import Optional, Dict, Any
from abc import ABC, abstractmethod
import asyncio
from typing_extensions import TypedDict, Protocol


# Suppress the pylint warning for too few public methods
# pylint: disable=R0903


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


T = TypeVar("T")


class Processor:
    """Class processor"""

    def __init__(self, data: List[T]) -> None:
        """init method"""
        self.data = data

    def apply(self, function: Callable[[T], T]) -> List[T]:
        """Apply method"""
        return [function(item) for item in self.data]


class FinalMeta(type):
    """Metaclass that prevents subclassing"""

    def __new__(mcs, name, bases, dct):
        if name != "Config" and any(
                issubclass(base, Config) for base in bases):
            raise TypeError(f"'{name}' class cannot be inherit from 'Config'")
        return super().__new__(mcs, name, bases, dct)


class Config(metaclass=FinalMeta):
    """Configuration class that cannot be inherited."""


class BaseRepository(ABC):
    """Abstract class for repositories with a save method."""

    @abstractmethod
    def save(self, data: Dict[str, Any]) -> None:
        """Abstract method to save data."""


class SQLRepository(BaseRepository):
    """Repository for saving data to an SQL database."""

    def save(self, data: Dict[str, Any]) -> None:
        """Implementation of the save method for SQL."""
        print(f"Saving data to SQL: {data}")


class AsyncFetcher:
    """Class AsyncFetcher"""

    @staticmethod
    async def fetch(url: str) -> Dict[str, Any]:
        """Method fetch"""
        await asyncio.sleep(1)
        return {"result_code": 200, "url": f"{url}",
                "data": "information_fetched"}
