import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Insert data
cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
               ("Ankit", 21, 89.5))
cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
               ("Riya", 22, 91.0))

conn.commit()
print("✅ Records inserted successfully!")

conn.close()
