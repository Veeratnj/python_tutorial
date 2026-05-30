"""
Generators

Example and comments for Generators.
"""

# Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(3):
    print(value)
