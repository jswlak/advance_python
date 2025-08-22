# Modern UI with ttkbootstrap

# first instll -- pip install ttkbootstrap

import ttkbootstrap as tb
from ttkbootstrap.constants import *

class ThemedApp(tb.Window):
    def __init__(self):
        super().__init__(themename="superhero")  # try 'flatly', 'darkly', 'cosmo'
        self.title("Tkinter with ttkbootstrap")
        self.geometry("400x250")

        label = tb.Label(self, text="Modern Tkinter UI", font=("Arial", 16))
        label.pack(pady=20)

        entry = tb.Entry(self, width=30)
        entry.pack(pady=10)

        button = tb.Button(self, text="Click Me", bootstyle=SUCCESS, command=lambda: label.config(text=f"Hello {entry.get()}!"))
        button.pack(pady=10)

if __name__ == "__main__":
    app = ThemedApp()
    app.mainloop()




'''
👉 You’ll get:

Modern styled widgets.

Multiple built-in themes.

Bootstrapped colors like SUCCESS, DANGER, INFO
'''
