import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

# Insert
cur.execute("INSERT INTO teacher (name, subject) VALUES (?, ?)", ("Anita", "Math"))
cur.execute("INSERT INTO teacher (name, subject) VALUES (?, ?)", ("Rajesh", "Science"))

# Fetch
cur.execute("SELECT * FROM teacher")
rows = cur.fetchall()

print("Teacher Table:")
for row in rows:
    print(row)

conn.commit()
conn.close()
