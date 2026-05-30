"""
Regular Expressions

Example and comments for Regular Expressions.
"""

# Regular Expressions
import re
pattern = re.compile(r"\d+")
print(pattern.findall("123 abc 456"))
