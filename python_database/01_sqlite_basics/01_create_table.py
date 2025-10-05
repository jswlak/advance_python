import sqlite3

# Connect to (or create) database
conn = sqlite3.connect('students.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    marks REAL
)
''')

conn.commit()
print("✅ Table 'students' created successfully!")

# Close connection
conn.close()
