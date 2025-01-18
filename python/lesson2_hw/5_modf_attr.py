class MutableClass:
    def add_attribute(self, name, value):
        setattr(self, name, value)

    def remove_attribute(self, name):
        delattr(self, name)


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")
#print(obj.name)  # Виникне помилка, атрибут видалений