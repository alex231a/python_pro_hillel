class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        attr = getattr(self._obj, name)

        if callable(attr):
            def wrapper(*args, **kwargs):
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