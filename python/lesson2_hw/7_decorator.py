from typing import Any, Callable, Type


def log_methods(cls: Type):
    """A class decorator that wraps all callable methods (excluding dunder
    methods)
    with logging functionality."""

    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith('__'):
            def create_wrapper(attr_value: Callable[..., Any], attr_name: str):
                """Creates a wrapper function that logs the method calls and
                their arguments."""

                def wrapper(self: Any, *args: Any, **kwargs: Any):

                    """Wrapper function to log method calls."""

                    if not args:
                        args_to_log = ''
                    else:
                        args_to_log = args
                    if not kwargs:
                        kwargs_to_log = ''
                    else:
                        kwargs_to_log = kwargs
                    print(
                        f"Logging: {attr_name} called with: {args_to_log}, "
                        f"{kwargs_to_log}")
                    result = attr_value(self, *args, **kwargs)
                    return result

                return wrapper

            wrapped_method = create_wrapper(attr_value, attr_name)
            setattr(cls, attr_name, wrapped_method)

    return cls


@log_methods
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


obj = MyClass()
obj.add(5, 3)  # Logging: add called with (5, 3)
obj.subtract(5, 3)  # Logging: subtract called with (5, 3)
