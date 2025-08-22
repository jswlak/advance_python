# Treeview + SQLite Database

import tkinter as tk
from tkinter import ttk
import sqlite3

class DBTreeviewApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Treeview with SQLite")
        self.geometry("500x300")

        # Setup DB
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # Treeview
        self.tree = ttk.Treeview(self, columns=("Name", "Age"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Insert Data Button
        add_btn = tk.Button(self, text="Add Sample Data", command=self.add_data)
        add_btn.pack(pady=10)

        self.load_data()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS people (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                age INTEGER)""")
        self.conn.commit()

    def add_data(self):
        self.cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", ("John Doe", 25))
        self.conn.commit()
        self.load_data()

    def load_data(self):
        # Clear old data
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insert new data
        self.cursor.execute("SELECT name, age FROM people")
        for row in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=row)

if __name__ == "__main__":
    app = DBTreeviewApp()
    app.mainloop()


'''Treeview widget (tabular data).

SQLite integration with Tkinter.

Refreshing tree after DB updates.
'''

