import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Entry Input Example")
root.geometry("400x200")

# Label for instructions
label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
label.pack(pady=10)

# Entry widget for input
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Output label
output_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
output_label.pack(pady=10)

# Function to display entered name
def show_name():
    name = entry.get()  # Get text from entry
    output_label.config(text=f"Hello, {name}!")

# Button to trigger action
button = tk.Button(root, text="Submit", command=show_name)
button.pack(pady=10)

# Start the app
root.mainloop()
