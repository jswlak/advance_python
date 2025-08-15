import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Information", "This is an info message.")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message!")

def show_error():
    messagebox.showerror("Error", "This is an error message!")

def ask_question():
    answer = messagebox.askquestion("Question", "Do you like Python?")
    if answer == 'yes':
        messagebox.showinfo("Response", "That's great!")
    else:
        messagebox.showinfo("Response", "Oh, that's sad.")

# Main window
root = tk.Tk()
root.title("Messagebox Demo")
root.geometry("300x300")

# Buttons
tk.Button(root, text="Show Info", command=show_info).pack(pady=5)
tk.Button(root, text="Show Warning", command=show_warning).pack(pady=5)
tk.Button(root, text="Show Error", command=show_error).pack(pady=5)
tk.Button(root, text="Ask Question", command=ask_question).pack(pady=5)

root.mainloop()
