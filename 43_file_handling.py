"""
File Handling

Example and comments for File Handling.
"""

# File Handling
path = Path("sample.txt")
path.write_text("Hello file")
print(path.read_text())
