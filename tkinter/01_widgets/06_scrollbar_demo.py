import tkinter as tk

root = tk.Tk()
root.title("Scrollbar Demo")

text = tk.Text(root, wrap="word", width=40, height=10)
scrollbar = tk.Scrollbar(root, command=text.yview)
text.config(yscrollcommand=scrollbar.set)

text.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Add sample text
for i in range(1, 51):
    text.insert(tk.END, f"Line {i}\n")

root.mainloop()





'''
Key Points:

Scrollbars can be linked to Text, Canvas, Listbox, or even Treeview.

yscrollcommand connects widget to scrollbar.

'''