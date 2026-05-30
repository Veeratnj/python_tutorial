"""
Mocking

Example and comments for Mocking.
"""

# Mocking
# Requires unittest.mock
from unittest.mock import MagicMock
obj = MagicMock()
obj.method.return_value = 10
print(obj.method())
