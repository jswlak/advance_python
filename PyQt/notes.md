# 🧩 PyQt Notes — GUI Framework

## 📘 Overview
**PyQt** is a set of Python bindings for the **Qt framework**, a popular cross-platform GUI toolkit developed in C++.  
It allows developers to build **desktop applications** with a **native look and feel** for Windows, macOS, and Linux.

---

## ⚙️ Installation

```bash
pip install PyQt5
```

To verify:
```bash
python -m PyQt5.QtCore
```

Optional (for UI designer):
```bash
pip install PyQt5-tools
```

---

## 🧠 Key Components

| Module | Description |
|--------|--------------|
| `QtWidgets` | Contains GUI widgets (buttons, text boxes, labels, etc.) |
| `QtCore` | Core non-GUI functionality (signals, slots, timers, etc.) |
| `QtGui` | Handles graphics, fonts, and images |
| `QtMultimedia` | Audio, video, and multimedia features |
| `QtNetwork` | Networking and communication |
| `QtChart` | Data visualization and charts |
| `QtDesigner` | GUI design tool to visually create layouts |

---

## 🏗️ Basic Structure of a PyQt App

```python
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)       # Create the application object

window = QWidget()                 # Create main window
window.setWindowTitle("My First PyQt App")
window.setGeometry(100, 100, 300, 200)

label = QLabel("Hello, PyQt!", parent=window)
label.move(100, 80)

window.show()                      # Display the window
sys.exit(app.exec_())              # Start the event loop
```

---

## 🪟 Common Widgets

| Widget | Description |
|---------|--------------|
| `QLabel` | Displays text or image |
| `QPushButton` | Button widget |
| `QLineEdit` | Single-line text input |
| `QTextEdit` | Multi-line text editor |
| `QCheckBox` | Checkbox option |
| `QRadioButton` | Radio button option |
| `QComboBox` | Drop-down menu |
| `QSlider` | Slider control |
| `QSpinBox` | Number input spinner |
| `QTableWidget` | Display tabular data |
| `QMessageBox` | Pop-up dialog box |

---

## 📐 Layout Management

PyQt uses **layout managers** to arrange widgets.

| Layout | Description |
|---------|--------------|
| `QHBoxLayout` | Horizontal layout |
| `QVBoxLayout` | Vertical layout |
| `QGridLayout` | Grid-like layout |
| `QFormLayout` | Form-style layout (label + input pairs) |

### Example:
```python
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

layout.addWidget(QPushButton('Button 1'))
layout.addWidget(QPushButton('Button 2'))
layout.addWidget(QPushButton('Button 3'))

window.setLayout(layout)
window.show()
app.exec_()
```

---

## 🔗 Signals and Slots

- **Signals:** Events emitted by widgets (e.g., button clicked)
- **Slots:** Functions that respond to those signals

### Example:
```python
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def on_click():
    print("Button clicked!")

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

btn = QPushButton("Click Me")
btn.clicked.connect(on_click)  # Connect signal to slot

layout.addWidget(btn)
window.setLayout(layout)
window.show()
app.exec_()
```

---

## 🎨 Styling (Using CSS)

You can style PyQt widgets using **Qt Style Sheets (QSS)** — similar to CSS.

```python
btn.setStyleSheet("""
    QPushButton {
        background-color: #0078D7;
        color: white;
        border-radius: 8px;
        padding: 6px 12px;
    }
    QPushButton:hover {
        background-color: #005A9E;
    }
""")
```

---

## 🧰 Designing GUI Visually

1. Install **Qt Designer** (`pip install pyqt5-tools`)
2. Open Designer:
   ```bash
   python -m PyQt5.uic
   ```
3. Create `.ui` file (drag-and-drop UI design)
4. Convert `.ui` → `.py`:
   ```bash
   pyuic5 -x design.ui -o design.py
   ```

---

## 💾 Working with Dialogs

### Example – Message Box
```python
from PyQt5.QtWidgets import QMessageBox

msg = QMessageBox()
msg.setWindowTitle("Info")
msg.setText("Operation Successful!")
msg.setIcon(QMessageBox.Information)
msg.exec_()
```

---

## 🖼️ Displaying Images

```python
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPixmap

app = QApplication([])
label = QLabel()
pixmap = QPixmap("image.png")
label.setPixmap(pixmap)
label.show()
app.exec_()
```

---

## ⚡ Advanced Topics

- **QTimer** — for scheduling repetitive actions  
- **QThread** — for running tasks in the background  
- **QFileDialog** — open/save file dialogs  
- **QTableView + QAbstractModel** — for large data sets  
- **QGraphicsView** — for custom 2D graphics  

---

## 📚 Resources

- [Official PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Qt for Python Tutorials](https://doc.qt.io/qtforpython/)
- [PyQt Examples Repo](https://github.com/baoboa/pyqt5)
