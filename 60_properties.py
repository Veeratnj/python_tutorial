"""
Properties

Example and comments for Properties.
"""

# Properties
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        self._temperature = value

obj = Celsius(25)
obj.temperature = 30
print(obj.temperature)
