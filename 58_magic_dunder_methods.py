"""
Magic/Dunder Methods

Example and comments for Magic/Dunder Methods.
"""

# Magic/Dunder Methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

print(Point(1, 2))
