class TypeCheckedMeta(type):
    def __new__(cls, name, bases, dct):
        annotations = dct.get('__annotations__', {})

        new_class = super().__new__(cls, name, bases, dct)

        for attr_name, attr_type in annotations.items():
            original_setattr = new_class.__setattr__

            def type_checked_setattr(self, name, value):
                if name in annotations and not isinstance(value, annotations[name]):
                    raise TypeError(f"For attribute '{name}' expected '{annotations[name].__name__}', got '{type(value).__name__}'.")
                super(type(self), self).__setattr__(name, value)

            new_class.__setattr__ = type_checked_setattr

        return new_class


class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


p = Person()
p.name = "John"  # Все добре
p.age = "30"  # Викличе помилку, очікується int

