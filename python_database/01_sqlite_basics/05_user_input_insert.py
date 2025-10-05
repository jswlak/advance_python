# Insert data dynamically from user input.

import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
               (name, age, marks))

conn.commit()
print(f"✅ Record added for {name}")

conn.close()
