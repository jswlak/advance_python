import json
import os

DATA_FILE = "mini_project/Inventory_management_system/inventory.json"


# -------------------------------
# Helper Functions
# -------------------------------
def load_data():
    """Load data from JSON file or return empty list if file not found"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []


def save_data(data):
    """Save data to JSON file"""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# -------------------------------
# CRUD Functions
# -------------------------------
def add_item():
    """Add a new inventory item"""
    items = load_data()
    name = input("Enter item name: ").strip()
    quantity = int(input("Enter quantity: ").strip())
    price = float(input("Enter price per unit: ").strip())

    item = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    items.append(item)
    save_data(items)
    print(f"✅ Item '{name}' added successfully!")


def view_inventory():
    """Display all inventory items"""
    items = load_data()
    if not items:
        print("⚠️ Inventory is empty!")
        return
    else:
        
        print("\n=== Inventory List ===")
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item['name']} - Qty: {item['quantity']} - Price: ₹{item['price']}")
        print("========================\n")


def update_quantity():
    """Update the quantity of an existing item"""
    items = load_data()
    name = input("Enter item name to update: ").strip()

    for item in items:
        if item["name"].lower() == name.lower():
            new_qty = int(input("Enter new quantity: ").strip())
            item["quantity"] = new_qty
            save_data(items)
            print(f"✅ Quantity updated for '{name}'!")
            return
    print("❌ Item not found!")

def delete_item():
    """Delete an item from inventory"""
    items = load_data()
    name = input("Enter item name to delete: ").strip()
    new_items = [item for item in items if item["name"].lower() != name.lower()]

    if len(new_items) == len(items):
        print("❌ Item not found!")
    else:
        save_data(new_items)
        print(f"🗑️ Item '{name}' deleted successfully!")

def main():
    """Main menu loop"""
    while True:
        print("\n=== Inventory Management ===")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Quantity")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
