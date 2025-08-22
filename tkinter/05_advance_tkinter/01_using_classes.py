# Tkinter with Classes (OOP style)

import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window config
        self.title("Tkinter OOP Example")
        self.geometry("400x250")

        # Label
        self.label = tk.Label(self, text="Hello, Tkinter with Classes!", font=("Arial", 14))
        self.label.pack(pady=20)

        # Entry
        self.entry = tk.Entry(self, width=30)
        self.entry.pack(pady=5)

        # Button
        self.button = tk.Button(self, text="Update Label", command=self.update_label)
        self.button.pack(pady=10)

    def update_label(self):
        text = self.entry.get()
        self.label.config(text=f"You typed: {text}")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()






'''
Why OOP?

    Keeps code organized.

    Easier to extend GUI with more windows & features.

    Standard approach for real projects.
'''
