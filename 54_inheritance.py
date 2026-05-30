"""
Inheritance

Example and comments for Inheritance.
"""

# Inheritance
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

Dog().speak()
