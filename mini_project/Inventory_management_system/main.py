#for gui

import tkinter as tk
from tkinter import ttk, messagebox
from inventory_core import add_item, get_inventory, update_quantity, delete_item

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📦 Inventory Management System")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.create_widgets()
        self.load_inventory()

    def create_widgets(self):
        # --- Input Frame ---
        frame = tk.LabelFrame(self.root, text="Add / Update Item", padx=10, pady=10)
        frame.pack(fill="x", padx=10, pady=10)

        tk.Label(frame, text="Item Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Quantity:").grid(row=0, column=2, padx=5, pady=5)
        self.qty_entry = tk.Entry(frame)
        self.qty_entry.grid(row=0, column=3, padx=5)

        tk.Label(frame, text="Price:").grid(row=0, column=4, padx=5, pady=5)
        self.price_entry = tk.Entry(frame)
        self.price_entry.grid(row=0, column=5, padx=5)

        tk.Button(frame, text="Add Item", command=self.add_item).grid(row=0, column=6, padx=10)
        tk.Button(frame, text="Update Qty", command=self.update_item).grid(row=0, column=7, padx=5)

        # --- Inventory Table ---
        self.tree = ttk.Treeview(self.root, columns=("Name", "Quantity", "Price"), show="headings", height=15)
        self.tree.heading("Name", text="Item Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price (₹)")
        self.tree.column("Name", width=200)
        self.tree.column("Quantity", width=100)
        self.tree.column("Price", width=100)
        self.tree.pack(padx=10, pady=10, fill="x")

        # --- Buttons ---
        tk.Button(self.root, text="Delete Selected", command=self.delete_selected, bg="red", fg="white").pack(pady=5)
        tk.Button(self.root, text="Refresh", command=self.load_inventory).pack()

    def add_item(self):
        name = self.name_entry.get().strip()
        qty = self.qty_entry.get().strip()
        price = self.price_entry.get().strip()

        if not name or not qty or not price:
            messagebox.showwarning("⚠️ Warning", "Please fill all fields!")
            return

        try:
            add_item(name, int(qty), float(price))
            messagebox.showinfo("✅ Success", f"Item '{name}' added successfully!")
            self.clear_inputs()
            self.load_inventory()
        except ValueError:
            messagebox.showerror("Error", "Quantity must be integer and Price must be a number.")

    def update_item(self):
        name = self.name_entry.get().strip()
        qty = self.qty_entry.get().strip()

        if not name or not qty:
            messagebox.showwarning("⚠️ Warning", "Enter item name and new quantity.")
            return

        try:
            updated = update_quantity(name, int(qty))
            if updated:
                messagebox.showinfo("✅ Updated", f"Quantity updated for '{name}'.")
                self.load_inventory()
            else:
                messagebox.showerror("❌ Not Found", "Item not found.")
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer.")

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("⚠️ Warning", "Select an item to delete.")
            return

        item_name = self.tree.item(selected[0])["values"][0]
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete '{item_name}'?")
        if confirm:
            if delete_item(item_name):
                messagebox.showinfo("🗑️ Deleted", f"Item '{item_name}' deleted successfully!")
                self.load_inventory()
            else:
                messagebox.showerror("❌ Error", "Item not found!")

    def load_inventory(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in get_inventory():
            self.tree.insert("", "end", values=(item["name"], item["quantity"], f"₹{item['price']}"))

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
