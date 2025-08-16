import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview Demo")

columns = ("Invoice ID", "Customer", "Amount")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Sample data
data = [
    (1, "John Doe", "$150"),
    (2, "Jane Smith", "$200"),
    (3, "David Johnson", "$300")
]

for item in data:
    tree.insert("", tk.END, values=item)

tree.pack(fill="both", expand=True)

root.mainloop()





# Key Points:

# Treeview is perfect for showing structured tabular data.

# insert() adds rows dynamically.

