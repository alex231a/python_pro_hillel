class LimitedAttributesMeta(type):
    def __new__(cls, name, bases, attrs):
        max_attrs = 3
        list_attr = [attr for attr in attrs if not attr.startswith('__')]
        if len(list_attr) > max_attrs:
            raise TypeError(
                f"Class {name} cannot have more than {max_attrs} attributes")

        return super().__new__(cls, name, bases, attrs)


class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3
    # attr4 = 4  # Викличе помилку


obj = LimitedClass()
