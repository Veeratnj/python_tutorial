"""
CSV Handling

Example and comments for CSV Handling.
"""

# CSV Handling
import csv
rows = [["name", "age"], ["Eva", 30]]
with open("sample.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("CSV written")
