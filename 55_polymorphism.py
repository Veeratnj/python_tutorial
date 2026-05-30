"""
Polymorphism

Example and comments for Polymorphism.
"""

# Polymorphism
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

for animal in (Cat(), Dog()):
    animal.speak()
