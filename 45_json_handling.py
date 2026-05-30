"""
JSON Handling

Example and comments for JSON Handling.
"""

# JSON Handling
import json
data = {"name": "Nina", "age": 32}
text = json.dumps(data)
print(text)
print(json.loads(text))
