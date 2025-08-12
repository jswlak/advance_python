import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Labels and Buttons")
root.geometry("400x200")

# Label widget
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 16))
label.pack(pady=10)

# Function to handle button click
def on_click():
    label.config(text="Button Clicked!")

# Button widget
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# Start the application
root.mainloop()
