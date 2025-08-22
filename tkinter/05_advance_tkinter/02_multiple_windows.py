'''
    Handling Multiple Windows
'''

import tkinter as tk
from tkinter import Toplevel

class MultiWindowApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("300x200")

        tk.Label(self, text="This is the main window").pack(pady=20)

        open_btn = tk.Button(self, text="Open Child Window", command=self.open_child)
        open_btn.pack()

    def open_child(self):
        child = Toplevel(self)   # Creates a new window
        child.title("Child Window")
        child.geometry("250x150")
        tk.Label(child, text="This is the child window").pack(pady=20)

if __name__ == "__main__":
    app = MultiWindowApp()
    app.mainloop()
