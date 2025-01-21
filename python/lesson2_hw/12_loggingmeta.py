from typing import Any, Dict, Type


class LoggingMeta(type):
    """A metaclass for logging attribute access."""

    def __new__(cls: Type['LoggingMeta'], name: str, bases: tuple,
                dct: Dict[str, Any]):
        for key, value in list(dct.items()):
            if not key.startswith('__') and not callable(value):
                dct[key] = cls._create_property(key)
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def _create_property(attr_name: str):
        """Create a property for the given attribute name."""
        private_name = f"_{attr_name}"

        def getter(self: Any):
            print(f"Logging: accessed '{attr_name}'")
            if not hasattr(self, private_name):
                raise AttributeError(f"Attribute '{attr_name}' is not set.")
            return getattr(self, private_name)

        def setter(self: Any, value: Any):
            print(f"Logging: modified '{attr_name}'")
            setattr(self, private_name, value)

        def deleter(self: Any):
            print(f"Logging: deleted '{attr_name}'")
            if hasattr(self, private_name):
                delattr(self, private_name)
            else:
                raise AttributeError(f"Attribute '{attr_name}' is not set.")

        return property(getter, setter, deleter)

    def __call__(cls: Type['LoggingMeta'], *args: Any, **kwargs: Any):
        """ Wraps the instance of the class to log attribute access and
        modification."""
        instance = super().__call__(*args, **kwargs)
        return cls._wrap_instance(instance)

    @staticmethod
    def _wrap_instance(instance: Any):
        """Creates a wrapper class that logs changes to instance attributes."""

        class Wrapped(instance.__class__):
            def __setattr__(self: Any, name: str, value: Any):
                print(f"Logging: modified '{name}'")
                super().__setattr__(name, value)

            def __getattribute__(self: Any, name: str):
                if not name.startswith('_'):
                    print(f"Logging: accessed '{name}'")
                return super().__getattribute__(name)

            def __delattr__(self: Any, name: str):
                print(f"Logging: deleted '{name}'")
                super().__delattr__(name)

        instance.__class__ = Wrapped
        return instance


class MyClass(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name


obj = MyClass("Python")
print(obj.name)  # Logging: accessed 'name'
obj.name = "New Python"  # Logging: modified 'name'
