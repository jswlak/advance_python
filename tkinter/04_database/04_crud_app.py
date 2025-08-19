'''
04_crud_app.py   (merged full CRUD for inventory + customers)
'''

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------------
# Database Setup
# -------------------------------
conn = sqlite3.connect("accounting.db")
c = conn.cursor()

# Create tables if not exists
c.execute('''CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                quantity INTEGER,
                price REAL
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                phone TEXT
            )''')
conn.commit()


# -------------------------------
# CRUD Functions
# -------------------------------
def add_product():
    pname, qty, price = e_pname.get(), e_qty.get(), e_price.get()
    if pname and qty and price:
        c.execute("INSERT INTO inventory (product_name, quantity, price) VALUES (?, ?, ?)",
                  (pname, int(qty), float(price)))
        conn.commit()
        load_inventory()
        messagebox.showinfo("Success", "Product Added!")
    else:
        messagebox.showerror("Error", "Fill all fields!")


def add_customer():
    name, email, phone = e_cname.get(), e_cemail.get(), e_cphone.get()
    if name and email and phone:
        c.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)",
                  (name, email, phone))
        conn.commit()
        load_customers()
        messagebox.showinfo("Success", "Customer Added!")
    else:
        messagebox.showerror("Error", "Fill all fields!")


def load_inventory():
    for row in inventory_table.get_children():
        inventory_table.delete(row)
    for row in c.execute("SELECT * FROM inventory"):
        inventory_table.insert("", tk.END, values=row)


def load_customers():
    for row in customer_table.get_children():
        customer_table.delete(row)
    for row in c.execute("SELECT * FROM customers"):
        customer_table.insert("", tk.END, values=row)


# -------------------------------
# GUI
# -------------------------------
root = tk.Tk()
root.title("Mini Accounting App (CRUD)")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# --- Inventory Tab ---
frame_inventory = ttk.Frame(notebook)
notebook.add(frame_inventory, text="Inventory")

tk.Label(frame_inventory, text="Product").grid(row=0, column=0)
tk.Label(frame_inventory, text="Quantity").grid(row=0, column=1)
tk.Label(frame_inventory, text="Price").grid(row=0, column=2)

e_pname = tk.Entry(frame_inventory)
e_qty = tk.Entry(frame_inventory)
e_price = tk.Entry(frame_inventory)

e_pname.grid(row=1, column=0)
e_qty.grid(row=1, column=1)
e_price.grid(row=1, column=2)

tk.Button(frame_inventory, text="Add Product", command=add_product).grid(row=1, column=3)

inventory_table = ttk.Treeview(frame_inventory, columns=("ID", "Name", "Qty", "Price"), show="headings")
for col in ("ID", "Name", "Qty", "Price"):
    inventory_table.heading(col, text=col)
inventory_table.grid(row=2, column=0, columnspan=4)

# --- Customers Tab ---
frame_customers = ttk.Frame(notebook)
notebook.add(frame_customers, text="Customers")

tk.Label(frame_customers, text="Name").grid(row=0, column=0)
tk.Label(frame_customers, text="Email").grid(row=0, column=1)
tk.Label(frame_customers, text="Phone").grid(row=0, column=2)

e_cname = tk.Entry(frame_customers)
e_cemail = tk.Entry(frame_customers)
e_cphone = tk.Entry(frame_customers)

e_cname.grid(row=1, column=0)
e_cemail.grid(row=1, column=1)
e_cphone.grid(row=1, column=2)

tk.Button(frame_customers, text="Add Customer", command=add_customer).grid(row=1, column=3)

customer_table = ttk.Treeview(frame_customers, columns=("ID", "Name", "Email", "Phone"), show="headings")
for col in ("ID", "Name", "Email", "Phone"):
    customer_table.heading(col, text=col)
customer_table.grid(row=2, column=0, columnspan=4)

# Load Data Initially
load_inventory()
load_customers()

root.mainloop()






'''

Features - 

2 Tabs (Inventory + Customers)

Add Products, Add Customers

SQLite database persistence

Table view (Treeview) for both

'''