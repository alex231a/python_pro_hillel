from typing import Any, Dict, Type


class SingletonMeta(type):
    """A metaclass for implementing the Singleton pattern."""

    _instances: Dict[Type, Any] = {}

    def __call__(cls: Type['SingletonMeta'], *args: Any, **kwargs: Any):
        """Check whether instance already exists and return it if so."""

        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")


obj1 = Singleton()  # Creating instance
obj2 = Singleton()
print(obj1 is obj2)  # True
