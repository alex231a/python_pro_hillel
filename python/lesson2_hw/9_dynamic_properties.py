class DynamicProperties:
    def __init__(self):
        self._properties = {}

    def add_property(self, prop_name, default_value=None):
        self._properties[prop_name] = default_value

        def getter(self):
            return self._properties[prop_name]

        def setter(self, value):
            self._properties[prop_name] = value

        setattr(DynamicProperties, prop_name, property(getter, setter))



obj = DynamicProperties()
obj.add_property('name', 'default_name')
print(obj.name)  # default_name
obj.name = "Python"
print(obj.name)  # Python
