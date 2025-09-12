import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS teacher (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT
)
""")

print("Database and table created successfully!")
conn.commit()
conn.close()
