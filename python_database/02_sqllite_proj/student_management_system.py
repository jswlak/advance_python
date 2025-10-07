# Manages student data — add, view, search, update, delete.

import sqlite3

def connect_db():
    return sqlite3.connect('student_system.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        marks REAL
    )''')
    conn.commit()
    conn.close()

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
                   (name, age, marks))
    conn.commit()
    conn.close()
    print("✅ Student added successfully!")

def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    print("\n📋 Student List:")
    for r in rows:
        print(f"ID: {r[0]} | Name: {r[1]} | Age: {r[2]} | Marks: {r[3]}")
    print()

def search_student():
    name = input("Enter name to search: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",))
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("\n🔎 Search Results:")
        for r in rows:
            print(f"ID: {r[0]} | Name: {r[1]} | Age: {r[2]} | Marks: {r[3]}")
    else:
        print("❌ No student found!")

def update_marks():
    id_ = int(input("Enter student ID: "))
    marks = float(input("Enter new marks: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, id_))
    conn.commit()
    conn.close()
    print("✅ Marks updated!")

def delete_student():
    id_ = int(input("Enter student ID to delete: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (id_,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted!")

def menu():
    create_table()
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_marks()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
