"""
Scope: Global and Nonlocal

Example and comments for Scope: Global and Nonlocal.
"""

# Scope: Global and Nonlocal
count = 0

def outer():
    value = 1
    def inner():
        nonlocal value
        value += 1
        return value
    print(inner())

outer()
print(count)
