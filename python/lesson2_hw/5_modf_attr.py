from typing import Any


class MutableClass:
    """Class that allows adding and removing attributes dynamically."""

    def add_attribute(self, name: str, value: Any):
        """ Adds an attribute to the instance dynamically."""

        setattr(self, name, value)

    def remove_attribute(self, name: str):
        """Removes an attribute from the instance dynamically."""

        delattr(self, name)


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")
# print(obj.name)  # Виникне помилка, атрибут видалений
