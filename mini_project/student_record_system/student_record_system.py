import json
import os

DATA_FILE = "mini_project/student_record_system/students.json"


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
def add_student():
    data = load_data()
    roll = input("Enter Roll No: ").strip()

    # Prevent duplicate roll numbers
    if any(s["roll"] == roll for s in data):
        print("❌ Student with this Roll No already exists.")
        return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    marks = input("Enter Marks: ").strip()

    student = {"roll": roll, "name": name, "age": age, "marks": marks}
    data.append(student)
    save_data(data)
    print("✅ Student added successfully!")


def view_students():
    data = load_data()
    if not data:
        print("📭 No student records found.")
        return

    print("\n=== Student Records ===")
    for s in data:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")
    print("========================\n")


def search_student():
    roll = input("Enter Roll No to search: ").strip()
    data = load_data()

    for s in data:
        if s["roll"] == roll:
            print(f"\n🎯 Found Student:\nName: {s['name']}\nAge: {s['age']}\nMarks: {s['marks']}\n")
            return
    print("❌ Student not found.")


def update_student():
    roll = input("Enter Roll No to update: ").strip()
    data = load_data()

    for s in data:
        if s["roll"] == roll:
            print(f"Current Data: {s}")
            s["name"] = input(f"Enter new name ({s['name']}): ") or s["name"]
            s["age"] = input(f"Enter new age ({s['age']}): ") or s["age"]
            s["marks"] = input(f"Enter new marks ({s['marks']}): ") or s["marks"]
            save_data(data)
            print("✅ Student record updated successfully!")
            return
    print("❌ Student not found.")


def delete_student():
    roll = input("Enter Roll No to delete: ").strip()
    data = load_data()

    new_data = [s for s in data if s["roll"] != roll]
    if len(new_data) == len(data):
        print("❌ Student not found.")
    else:
        save_data(new_data)
        print("🗑️ Student deleted successfully!")


# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("""
=== 🎓 Student Record System ===
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting... Data saved successfully.")
            break
        else:
            print("⚠️ Invalid choice! Please enter between 1–6.")


if __name__ == "__main__":
    main()
