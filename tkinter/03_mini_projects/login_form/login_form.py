import tkinter as tk
from tkinter import messagebox

def login():
    user = entry_user.get()
    pwd = entry_pass.get()
    if user == "admin" and pwd == "1234":
        messagebox.showinfo("Login", "Login Successful ✅")
    else:
        messagebox.showerror("Login", "Invalid Username or Password ❌")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
