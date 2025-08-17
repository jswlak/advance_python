'''
Simple calculator:

Buttons for digits (0-9) & operators (+ - * /)

Entry (to display expression)

Equal (=) button to evaluate
'''

import tkinter as tk

def press(num):
    entry.insert(tk.END, num)

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, r, c) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, command=evaluate).grid(row=r, column=c, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, command=lambda t=text: press(t)).grid(row=r, column=c, padx=5, pady=5)

tk.Button(root, text="C", width=5, command=clear).grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()
