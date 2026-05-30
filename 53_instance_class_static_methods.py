"""
Instance, Class, and Static Methods

Example and comments for Instance, Class, and Static Methods.
"""

# Instance, Class, and Static Methods
class Example:
    counter = 0

    def __init__(self, value):
        self.value = value
        Example.counter += 1

    def instance_method(self):
        return self.value

    @classmethod
    def class_method(cls):
        return cls.counter

    @staticmethod
    def static_method():
        return "static"

obj = Example(5)
print(obj.instance_method(), Example.class_method(), Example.static_method())
