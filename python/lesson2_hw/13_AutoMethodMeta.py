class AutoMethodMeta(type):
    def __new__(cls, name, bases, dct):
        attrs_to_add = []
        for attr_name, attr_value in dct.items():
            if not attr_name.startswith('__'):
                attrs_to_add.append(attr_name)

        for attr_name in attrs_to_add:
            def getter(self, attr=attr_name):
                return getattr(self, attr)

            def setter(self, value, attr=attr_name):
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
