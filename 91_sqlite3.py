"""
SQLite3

Example and comments for SQLite3.
"""

# SQLite3
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE sample(id INTEGER)")
c.execute("INSERT INTO sample(id) VALUES(1)")
conn.commit()
print(list(c.execute("SELECT * FROM sample")))
conn.close()
