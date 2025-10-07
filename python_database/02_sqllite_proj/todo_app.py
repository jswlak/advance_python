# A personal task manager — add, mark done, view tasks.

import sqlite3

def connect_db():
    return sqlite3.connect('todo.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status TEXT DEFAULT 'Pending'
    )
    ''')
    conn.commit()
    conn.close()

def add_task():
    task = input("Enter new task: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    print("📝 Task added!")

def view_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    print("\n📋 To-Do List:")
    for r in rows:
        print(f"ID: {r[0]} | Task: {r[1]} | Status: {r[2]}")

def mark_done():
    id_ = int(input("Enter task ID to mark done: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'Done' WHERE id = ?", (id_,))
    conn.commit()
    conn.close()
    print("✅ Task marked as done!")

def delete_task():
    id_ = int(input("Enter task ID to delete: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id_,))
    conn.commit()
    conn.close()
    print("🗑️ Task deleted!")

def menu():
    create_table()
    while True:
        print("\n===== To-Do App =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    menu()
