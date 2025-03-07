from typing import Any


def call_function(obj: str, method_name: str, *args: Any):
    """Call method of object with given name and arguments"""

    if not obj.__getattribute__(method_name):
        raise AttributeError(f"Object {obj} has no method {method_name}")
    return obj.__getattribute__(method_name)(*args)


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()
print(call_function(calc, "add", 10, 5))  # 15
print(call_function(calc, "subtract", 10, 5))  # 5
