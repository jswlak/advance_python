# 📂 Advanced Tkinter Examples

This folder contains **advanced Tkinter examples** demonstrating best practices like OOP structure, multiple windows, database integration, and modern theming.

---

## 📌 Files Overview

### 1️⃣ `01_using_classes.py`
Build Tkinter apps using **Object-Oriented Programming (OOP)** for cleaner and more maintainable code.

**Key Concepts:**
- Inheriting from `tk.Tk`
- Encapsulating widgets & logic into a class
- Organizing UI methods

---

### 2️⃣ `02_multiple_windows.py`
Create and manage **multiple windows** with `Toplevel()`.

**Key Concepts:**
- Difference between `Tk()` (main window) and `Toplevel()` (child window)
- Handling parent-child window relationships
- Keeping the main window active

---

### 3️⃣ `03_treeview_with_db.py`
Integrate a **Treeview widget** with an **SQLite database** to display and manage tabular data.

**Key Concepts:**
- Using `ttk.Treeview` for structured data
- Connecting Tkinter to SQLite (`sqlite3`)
- Loading and refreshing data dynamically

---

### 4️⃣ `04_ttkbootstrap_theme.py`
Apply **modern themes and styles** using [ttkbootstrap](https://ttkbootstrap.readthedocs.io/).

**Key Concepts:**
- `ttkbootstrap.Window` for themed apps
- Switching themes like `"superhero"`, `"cosmo"`, `"darkly"`
- Using Bootstyle colors (`SUCCESS`, `DANGER`, `INFO`, etc.)

---

## 🚀 How to Run

1. Navigate to this folder:
   ```bash
   cd 05_advance_tkinter

2. Install dependencies (only required for the last example):
    ```bash
    pip install ttkbootstrap

3. Run any script:
    ```bash
    python 01_using_classes.py
