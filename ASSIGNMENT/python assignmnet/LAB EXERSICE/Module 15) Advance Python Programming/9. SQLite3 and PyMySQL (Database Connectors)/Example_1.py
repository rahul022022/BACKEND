# Program: SQLite3 connect, create table, insert, fetch

import sqlite3

# 1. Connect to database (it will create file if not exists)
conn = sqlite3.connect("students.db")

# 2. Create cursor
cur = conn.cursor()

# 3. Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# 4. Insert data
cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Rahul", 21))
cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Priya", 22))

# 5. Fetch data
cur.execute("SELECT * FROM students")
rows = cur.fetchall()

print("Students Table:")
for row in rows:
    print(row)

# 6. Commit and close
conn.commit()
conn.close()
