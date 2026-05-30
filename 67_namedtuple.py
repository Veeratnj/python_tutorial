"""
Namedtuple

Example and comments for Namedtuple.
"""

# Namedtuple
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)
