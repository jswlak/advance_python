import tkinter as tk

def add_product():
    name = entry_name.get()
    price = entry_price.get()
    qty = entry_qty.get()
    if name and price and qty:
        listbox.insert(tk.END, f"{name} - ₹{price} x {qty}")
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_qty.delete(0, tk.END)

root = tk.Tk()
root.title("Product Entry Form")
root.geometry("400x300")

tk.Label(root, text="Product Name").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Price").pack(pady=5)
entry_price = tk.Entry(root)
entry_price.pack(pady=5)

tk.Label(root, text="Quantity").pack(pady=5)
entry_qty = tk.Entry(root)
entry_qty.pack(pady=5)

tk.Button(root, text="Add Product", command=add_product).pack(pady=10)

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

root.mainloop()
