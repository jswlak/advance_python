import tkinter as tk
from tkinter import ttk

def show_selection():
    print("Selected customer:", customer_combo.get())

root = tk.Tk()
root.title("Combobox Demo")

customer_combo = ttk.Combobox(root, values=["John Doe", "Jane Smith", "David Johnson"])
customer_combo.pack(padx=10, pady=10)
customer_combo.set("Select Customer")

btn = tk.Button(root, text="Show Selection", command=show_selection)
btn.pack(pady=10)

root.mainloop()






# Key Points:

# ttk.Combobox is from tkinter.ttk (the themed widgets library).

# .set() sets default text.

# .get() retrieves the selected value.

