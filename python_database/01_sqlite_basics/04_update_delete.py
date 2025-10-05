# update and delete in database

import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Update record
cursor.execute("UPDATE students SET marks = ? WHERE name = ?", (95, "Ankit"))
print("✅ Marks updated for Ankit")

# Delete record
cursor.execute("DELETE FROM students WHERE name = ?", ("Riya",))
print("🗑️ Record deleted for Riya")

conn.commit()
conn.close()
