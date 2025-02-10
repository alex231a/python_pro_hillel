"""Module docstring"""
from abc import ABC, abstractmethod
from typing import Dict, Any


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


if __name__ == "__main__":
    repo = SQLRepository()
    repo.save({"name": "Product1", "price": 10.5})

    try:
        class AnotherConfig(Config):
            """Create new class"""
    except TypeError as e:
        print(f"Error: {e}")
