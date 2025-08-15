import tkinter as tk

def show_selection():
    selected = []
    if var_gst.get():
        selected.append("Include GST")
    if var_email.get():
        selected.append("Send Email Copy")
    print("Selected options:", selected)

root = tk.Tk()
root.title("Checkbutton Demo")

# Variables to hold checkbox states
var_gst = tk.BooleanVar()
var_email = tk.BooleanVar()

chk1 = tk.Checkbutton(root, text="Include GST", variable=var_gst)
chk1.pack(anchor="w", padx=10, pady=5)

chk2 = tk.Checkbutton(root, text="Send Email Copy", variable=var_email)
chk2.pack(anchor="w", padx=10, pady=5)

btn = tk.Button(root, text="Show Selection", command=show_selection)
btn.pack(pady=10)

root.mainloop()





#Key Points:

# BooleanVar() tracks if the box is checked (True) or not (False).

# .get() reads the state.

