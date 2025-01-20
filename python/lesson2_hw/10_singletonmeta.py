class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")


obj1 = Singleton()  # Creating instance
obj2 = Singleton()
print(obj1 is obj2)  # True