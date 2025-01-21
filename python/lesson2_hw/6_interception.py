from typing import Any


class Proxy:
    """A proxy class that wraps an object and logs method calls with their
    arguments."""

    def __init__(self, obj: Any):
        self._obj = obj

    def __getattr__(self, name: str):

        """Retrieves an attribute from the proxied object. If the attribute
        is callable,
        it wraps it to log calls and arguments."""

        attr = getattr(self._obj, name)

        if callable(attr):
            def wrapper(*args: Any, **kwargs: Any):

                """Wrapper function to log method calls and arguments."""

                if not args:
                    args_to_log = ''
                else:
                    args_to_log = args
                if not kwargs:
                    kwargs_to_log = ''
                else:
                    kwargs_to_log = kwargs
                print("Calling method: ")
                print(f"{name} with args: {args_to_log}, {kwargs_to_log}")
                return attr(*args, **kwargs)

            return wrapper
        return attr


class MyClass:
    def greet(self, name):
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))
