"""
Testing with Unittest

Example and comments for Testing with Unittest.
"""

# Testing with Unittest
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

print("Define unittest.TestCase classes and run tests.")
