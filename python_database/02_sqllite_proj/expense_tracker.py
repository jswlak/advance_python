# Track daily expenses with categories and totals.



import sqlite3

def connect_db():
    return sqlite3.connect('expenses.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL,
        note TEXT,
        date TEXT
    )
    ''')
    conn.commit()
    conn.close()

def add_expense():
    category = input("Enter category (Food/Travel/Other): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")
    date = input("Enter date (YYYY-MM-DD): ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (category, amount, note, date) VALUES (?, ?, ?, ?)",
                   (category, amount, note, date))
    conn.commit()
    conn.close()
    print("✅ Expense added!")

def view_expenses():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    print("\n💵 All Expenses:")
    for r in rows:
        print(f"ID: {r[0]} | Category: {r[1]} | Amount: {r[2]} | Note: {r[3]} | Date: {r[4]}")
    print()

def total_by_category():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    conn.close()

    print("\n📊 Total by Category:")
    for r in rows:
        print(f"{r[0]}: ₹{r[1]}")

def delete_expense():
    id_ = int(input("Enter expense ID to delete: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (id_,))
    conn.commit()
    conn.close()
    print("🗑️ Expense deleted!")

def menu():
    create_table()
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total by Category")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("👋 Exiting Expense Tracker...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    menu()
