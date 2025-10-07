# A mini CLI app for Create, Read, Update, Delete , CRUD



import sqlite3

def connect_db():
    return sqlite3.connect('students.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        age INTEGER,
                        marks REAL)''')
    conn.commit()
    conn.close()

def insert_student():
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

    print("\n📋 All Students:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Marks: {row[3]}")
    print()

def update_student():
    id_ = int(input("Enter student ID to update: "))
    new_marks = float(input("Enter new marks: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (new_marks, id_))
    conn.commit()
    conn.close()
    print("✅ Marks updated successfully!")

def delete_student():
    id_ = int(input("Enter student ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (id_,))
    conn.commit()
    conn.close()
    print("🗑️ Record deleted successfully!")

def menu():
    create_table()
    while True:
        print("\n===== Student Database Menu =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    menu()
