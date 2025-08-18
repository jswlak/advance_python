import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# -------------------------
# Database Setup
# -------------------------
def init_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# -------------------------
# CRUD Operations
# -------------------------
def add_product():
    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    if not name or not quantity or not price:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)",
                   (name, int(quantity), float(price)))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Product added successfully!")
    clear_fields()
    fetch_products()

def fetch_products():
    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

def update_product():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a product to update")
        return

    item = tree.item(selected)
    product_id = item["values"][0]

    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    if not name or not quantity or not price:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=?, quantity=?, price=? WHERE id=?",
                   (name, int(quantity), float(price), product_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Product updated successfully!")
    clear_fields()
    fetch_products()

def delete_product():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a product to delete")
        return

    item = tree.item(selected)
    product_id = item["values"][0]

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Deleted", "Product deleted successfully!")
    fetch_products()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)

# -------------------------
# UI Setup
# -------------------------
root = tk.Tk()
root.title("Inventory Management - CRUD")
root.geometry("600x400")

# Labels and Entries
tk.Label(root, text="Product Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Price:").grid(row=2, column=0, padx=10, pady=5)
entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Product", command=add_product).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Update Product", command=update_product).grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Delete Product", command=delete_product).grid(row=3, column=2, padx=10, pady=5)

# Treeview (Table)
columns = ("ID", "Name", "Quantity", "Price")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Initialize DB and load data
init_db()
fetch_products()

root.mainloop()
