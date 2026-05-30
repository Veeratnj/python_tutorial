"""
Decorators

Example and comments for Decorators.
"""

# Decorators
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper

@simple_decorator
def say_hi():
    print("Hi")

say_hi()
