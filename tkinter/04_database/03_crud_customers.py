import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# -------------------------------
# Database Setup
# -------------------------------
conn = sqlite3.connect("app_database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT
)
""")
conn.commit()

# -------------------------------
# Tkinter GUI
# -------------------------------
root = tk.Tk()
root.title("Customer Management")
root.geometry("600x400")

# --- Form Fields ---
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_phone = tk.Entry(root)
entry_phone.grid(row=2, column=1, padx=10, pady=5)

# --- Treeview (Table) ---
tree = ttk.Treeview(root, columns=("ID", "Name", "Email", "Phone"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Email", text="Email")
tree.heading("Phone", text="Phone")
tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=5, column=3, sticky="ns")

# -------------------------------
# Functions
# -------------------------------
def add_customer():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()

    if not name or not email:
        messagebox.showwarning("Input Error", "Name and Email are required!")
        return

    try:
        cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        conn.commit()
        messagebox.showinfo("Success", "Customer added successfully!")
        fetch_customers()
        clear_fields()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists!")

def fetch_customers():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM customers")
    for customer in cursor.fetchall():
        tree.insert("", "end", values=customer)

def delete_customer():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select a customer to delete!")
        return
    customer_id = tree.item(selected[0])["values"][0]
    cursor.execute("DELETE FROM customers WHERE id=?", (customer_id,))
    conn.commit()
    fetch_customers()

def update_customer():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select a customer to update!")
        return

    customer_id = tree.item(selected[0])["values"][0]
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()

    cursor.execute("UPDATE customers SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, customer_id))
    conn.commit()
    messagebox.showinfo("Updated", "Customer updated successfully!")
    fetch_customers()
    clear_fields()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# -------------------------------
# Buttons
# -------------------------------
tk.Button(root, text="Add", command=add_customer).grid(row=3, column=0, pady=10)
tk.Button(root, text="Update", command=update_customer).grid(row=3, column=1, pady=10)
tk.Button(root, text="Delete", command=delete_customer).grid(row=3, column=2, pady=10)
tk.Button(root, text="Clear", command=clear_fields).grid(row=3, column=3, pady=10)

# Load data on startup
fetch_customers()

root.mainloop()
