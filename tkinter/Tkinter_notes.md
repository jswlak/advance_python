
# 🪟 Tkinter Notes (Python GUI Library)

## 📘 1. Introduction
- **Tkinter** is Python’s built-in library for creating **Graphical User Interfaces (GUI)**.
- It’s lightweight, cross-platform, and included with Python.
- Works on Windows, macOS, and Linux.

```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My App")
root.geometry("400x300")  # width x height
root.mainloop()
```

---

## 🧩 2. Main Components (Widgets)

| Widget | Description | Example |
|---------|--------------|----------|
| `Label` | Displays text or image | `tk.Label(root, text="Hello").pack()` |
| `Button` | Creates a clickable button | `tk.Button(root, text="Click", command=func).pack()` |
| `Entry` | Single-line text input | `tk.Entry(root).pack()` |
| `Text` | Multi-line text area | `tk.Text(root).pack()` |
| `Checkbutton` | Checkbox | `tk.Checkbutton(root, text="Agree").pack()` |
| `Radiobutton` | Radio option | `tk.Radiobutton(root, text="Male", value=1).pack()` |
| `Listbox` | List of selectable items | `tk.Listbox(root).pack()` |
| `Frame` | Container for grouping widgets | `tk.Frame(root).pack()` |
| `Canvas` | Drawing shapes, images | `tk.Canvas(root, width=200, height=200).pack()` |
| `Menu` | Menu bar creation | `tk.Menu(root)` |

---

## 🧱 3. Geometry Managers

| Method | Description | Example |
|---------|--------------|----------|
| `.pack()` | Simple, stacks widgets vertically/horizontally | `label.pack(side="left")` |
| `.grid()` | Table-like layout | `label.grid(row=0, column=1)` |
| `.place()` | Absolute positioning | `label.place(x=50, y=100)` |

> Do not mix `pack()` and `grid()` in the same frame.

---

## ⚙️ 4. Event Handling

```python
def on_click(event):
    print("Mouse clicked!")

btn = tk.Button(root, text="Click Me")
btn.pack()
btn.bind("<Button-1>", on_click)  # Left click
```

Common events:
- `<Button-1>` → Left mouse click  
- `<Button-3>` → Right click  
- `<KeyPress>` → Key pressed  
- `<Enter>` / `<Leave>` → Mouse enters/leaves widget

---

## 🧠 5. Variables (Tkinter Variable Classes)

| Type | Used For | Example |
|------|-----------|----------|
| `StringVar()` | Text | `name = tk.StringVar()` |
| `IntVar()` | Integers | `age = tk.IntVar()` |
| `DoubleVar()` | Floats | `price = tk.DoubleVar()` |
| `BooleanVar()` | True/False | `status = tk.BooleanVar()` |

```python
name = tk.StringVar()
tk.Entry(root, textvariable=name).pack()
tk.Label(root, textvariable=name).pack()
```

---

## 🎨 6. Styling Widgets

```python
label = tk.Label(root, text="Hello", fg="blue", bg="yellow",
                 font=("Arial", 16, "bold"))
label.pack()
```

Common options:
- `fg` – Text color  
- `bg` – Background color  
- `font=("FontName", size, style)`  
- `padx`, `pady` – Padding  
- `relief="groove"` or `"sunken"` for border effects  

---

## 📂 7. Messagebox

```python
from tkinter import messagebox

messagebox.showinfo("Title", "Information message")
messagebox.showwarning("Warning", "Be careful!")
messagebox.showerror("Error", "Something went wrong")
```

---

## 🧭 8. Menus

```python
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
```

---

## 📊 9. Frames and Layouts

```python
top_frame = tk.Frame(root)
top_frame.pack()

bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom")
```

---

## 📋 10. File Dialogs

```python
from tkinter import filedialog

file_path = filedialog.askopenfilename(title="Select a file")
save_path = filedialog.asksaveasfilename(defaultextension=".txt")
```

---

## 🔁 11. Updating Widgets Dynamically

```python
def change_text():
    label.config(text="Updated!")

btn = tk.Button(root, text="Click", command=change_text)
label = tk.Label(root, text="Old Text")
label.pack()
btn.pack()
```

---

## 💾 12. Connecting Database (SQLite)

```python
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("INSERT INTO users (name) VALUES (?)", ("Ankit",))
conn.commit()
conn.close()
```

---

## 🧩 13. Useful Shortcuts

| Action | Method |
|--------|---------|
| Close window | `root.destroy()` |
| Get Entry value | `entry.get()` |
| Set Entry value | `entry.insert(0, "text")` |
| Clear Entry | `entry.delete(0, tk.END)` |
| Update Label | `label.config(text="New")` |

---

## 🚀 14. Mini Example

```python
import tkinter as tk
from tkinter import messagebox

def greet():
    name = entry.get()
    messagebox.showinfo("Greeting", f"Hello, {name}!")

root = tk.Tk()
root.title("Greeting App")

tk.Label(root, text="Enter your name:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
tk.Button(root, text="Greet", command=greet).pack(pady=10)

root.mainloop()
```
