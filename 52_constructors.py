"""
Constructors

Example and comments for Constructors.
"""

# Constructors
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Leo", 25)
print(p.name, p.age)
