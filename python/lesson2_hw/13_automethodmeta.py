from typing import Dict, Type, Any


class AutoMethodMeta(type):
    """A metaclass that automatically adds getter and setter methods for each
    attribute of the class."""

    def __new__(cls: Type['AutoMethodMeta'], name: str, bases: tuple,
                dct: Dict[str, Any]):
        """ Adds getter and setter methods for each non-special attribute in
        the class."""
        attrs_to_add = []
        for attr_name, attr_value in dct.items():
            if not attr_name.startswith('__'):
                attrs_to_add.append(attr_name)

        for attr_name in attrs_to_add:
            def getter(self: Any, attr=attr_name):
                """Getter method for an attribute."""
                return getattr(self, attr)

            def setter(self: Any, value: Any, attr=attr_name):
                """Setter method for an attribute."""
                setattr(self, attr, value)

            dct[f'get_{attr_name}'] = getter
            dct[f'set_{attr_name}'] = setter

        return super().__new__(cls, name, bases, dct)


class Person(metaclass=AutoMethodMeta):
    name = "John"
    age = 30


p = Person()
print(p.get_name())
p.set_age(31)
print(p.get_age())
