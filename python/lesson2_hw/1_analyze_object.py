def analyze_object(obj_in: object):
    """function that analyzes an object"""

    print(f"Object type:\n - {type(obj)}")
    print()
    print("Attributes and methods: ")
    for attr in dir(obj):
        if not attr.startswith("__"):
            print(f" - {attr}: {type(getattr(obj, attr))}")


class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)
