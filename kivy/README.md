# What is Kivy?

    Kivy is a Python framework for building cross-platform GUI apps.

    You can write once, and run on Windows, macOS, Linux, Android, iOS.

    It uses OpenGL for graphics, so it’s good for modern UIs and touch-based apps.

# Install Kivy:
    pip install "kivy[base]" kivy_examples

---

# Kivy Foundations — Widgets & Layouts

Think of it like **Lego**:  

- **Widgets** = individual blocks (e.g., `Button`, `Label`, `TextInput`, etc.)  
- **Layouts** = containers that arrange widgets together  

---

## Core Widgets

Here are the most important widgets you’ll use all the time:

| **Widget**    | **Purpose**                      |
|---------------|----------------------------------|
| `Label`       | Display text                     |
| `Button`      | Clickable button                 |
| `TextInput`   | Input text from user             |
| `CheckBox`    | True/False selection             |
| `Switch`      | On/Off toggle                    |
| `Slider`      | Choose a value from a range      |
| `Image`       | Display an image                 |
| `ProgressBar` | Show progress of a task          |

---

Example 00 - Label + Button + TextInput
visit - 00_hello_input.py

# Layout Managers

**Layouts** control how widgets are arranged inside your app.  
Think of them as **containers** that decide *where* each widget goes.  

---

## Common Layout Managers

### 1. BoxLayout → Linear (Horizontal / Vertical)
Arranges widgets in a straight line.

```python
BoxLayout(orientation="horizontal")  # side by side
BoxLayout(orientation="vertical")    # top to bottom
'''


