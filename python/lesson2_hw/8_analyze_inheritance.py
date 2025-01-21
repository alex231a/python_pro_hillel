import inspect
from typing import Type


def analyze_inheritance(cls: Type):
    """Analyzes a given class and prints methods inherited from its base
    classes"""

    print(f"Class {cls.__name__} inherits:")

    for base_class in inspect.getmro(cls)[1:]:
        for name, obj in inspect.getmembers(base_class):
            if inspect.isfunction(obj) and not name.startswith("_"):
                if name not in cls.__dict__:
                    print(f"- {name} from {base_class.__name__}")


class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


analyze_inheritance(Child)
