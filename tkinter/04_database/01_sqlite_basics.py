import sqlite3
import tkinter as tk
from tkinter import messagebox

# ----------------------------
# Database Setup
# ----------------------------
def init_db():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Create a simple table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ----------------------------
# Insert Data Function
# ----------------------------
def insert_user():
    name = entry_name.get()
    email = entry_email.get()

    if name == "" or email == "":
        messagebox.showerror("Error", "All fields required!")
        return

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        messagebox.showinfo("Success", "User added successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists!")
    conn.close()

# ----------------------------
# Fetch Data Function
# ----------------------------
def fetch_users():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    text_box.delete("1.0", tk.END)  # clear old data
    for row in rows:
        text_box.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}\n")

# ----------------------------
# Tkinter UI
# ----------------------------
root = tk.Tk()
root.title("SQLite Basic Example")

# Name Entry
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Email Entry
tk.Label(root, text="Email:").grid(row=1, column=0, padx=5, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Add User", command=insert_user).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(root, text="Show Users", command=fetch_users).grid(row=3, column=0, columnspan=2, pady=5)

# Text Box to display users
text_box = tk.Text(root, width=50, height=10)
text_box.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Initialize DB
init_db()

root.mainloop()







'''
🔹 What This Does:
Creates app.db (SQLite database file in project folder).

Creates a users table if not already present.

Allows adding name + email through Tkinter UI.

Displays all users inside a Text widget.'''