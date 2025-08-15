import tkinter as tk

def show_choice():
    print("Selected payment method:", payment_method.get())

root = tk.Tk()
root.title("Radiobutton Demo")

payment_method = tk.StringVar(value="Cash")

methods = ["Cash", "Card", "UPI"]
for method in methods:
    tk.Radiobutton(root, text=method, variable=payment_method, value=method).pack(anchor="w", padx=10, pady=2)

btn = tk.Button(root, text="Show Choice", command=show_choice)
btn.pack(pady=10)

root.mainloop()






# Key Points:

# StringVar() stores the selected value.

# Only one radiobutton from the same variable group can be selected.

