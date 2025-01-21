from typing import Any, Dict, Optional


class DynamicProperties:
    """A class that allows dynamic addition of properties with getter and
    setter methods."""

    def __init__(self):
        self._properties: Dict[str, Any] = {}

    def add_property(self, prop_name: str,
                     default_value: Optional[Any] = None):
        """Adds a new property to the class with the specified name and an
        optional default value."""

        self._properties[prop_name] = default_value

        def getter(instance: "DynamicProperties"):
            """Getter function for the dynamically added property."""
            return self._properties[prop_name]

        def setter(instance: "DynamicProperties", value: Any):
            """Setter function for the dynamically added property."""
            self._properties[prop_name] = value

        setattr(DynamicProperties, prop_name, property(getter, setter))


obj = DynamicProperties()
obj.add_property('name', 'default_name')
print(obj.name)  # default_name
obj.name = "Python"
print(obj.name)  # Python
