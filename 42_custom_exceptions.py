"""
Custom Exceptions

Example and comments for Custom Exceptions.
"""

# Custom Exceptions
class MyError(Exception):
    pass

try:
    raise MyError("Custom error occurred")
except MyError as e:
    print(e)
