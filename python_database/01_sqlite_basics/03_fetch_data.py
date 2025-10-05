#Fetch and display all records.

import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("📋 Student Records:")
for row in rows:
    print(row)

conn.close()
