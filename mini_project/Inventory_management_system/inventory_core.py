import json
import os

DATA_FILE = "mini_project/Inventory_management_system/inventory.json"

def load_data():
    """Load data from JSON file or return empty list if file not found"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_data(data):
    """Save data to JSON file"""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_item(name, quantity, price):
    """Add a new inventory item"""
    items = load_data()
    items.append({"name": name, "quantity": quantity, "price": price})
    save_data(items)

def get_inventory():
    """Return all items"""
    return load_data()

def update_quantity(name, new_qty):
    """Update quantity for an item"""
    items = load_data()
    for item in items:
        if item["name"].lower() == name.lower():
            item["quantity"] = new_qty
            save_data(items)
            return True
    return False

def delete_item(name):
    """Delete item by name"""
    items = load_data()
    new_items = [i for i in items if i["name"].lower() != name.lower()]
    if len(new_items) == len(items):
        return False
    save_data(new_items)
    return True
