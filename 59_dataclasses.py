"""
Dataclasses

Example and comments for Dataclasses.
"""

# Dataclasses
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

print(Book("1984", "Orwell"))
