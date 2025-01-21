from typing import Dict, Type, Any


class TypeCheckedMeta(type):
    """A metaclass that adds type checking to the `__setattr__` method. It
    ensures
    that attributes are set only with values of the correct type,
    as specified in
    the class annotations."""

    def __new__(cls: Type['TypeCheckedMeta'], name: str, bases: tuple,
                dct: Dict[str, Any]):
        """Adds type checking for attributes based on the class annotations."""

        annotations = dct.get('__annotations__', {})

        new_class = super().__new__(cls, name, bases, dct)

        for attr_name, attr_type in annotations.items():
            original_setattr = new_class.__setattr__

            def type_checked_setattr(self: Any, name: str, value: Any):
                """Checks the type of the value being assigned to the
                attribute."""

                if name in annotations and not isinstance(value,
                                                          annotations[name]):
                    raise TypeError(
                        f"For attribute '{name}' expected '"
                        f"{annotations[name].__name__}', got '"
                        f"{type(value).__name__}'.")
                super(type(self), self).__setattr__(name, value)

            new_class.__setattr__ = type_checked_setattr

        return new_class


class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


p = Person()
p.name = "John"  # Все добре
p.age = "30"  # Викличе помилку, очікується int
