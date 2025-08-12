import tkinter as tk

root = tk.Tk()
root.title("Event Handling Demo")
root.geometry("400x250")

# Label to display messages
label = tk.Label(root, text="Click or type something...", font=("Arial", 14))
label.pack(pady=20)

# Function to handle mouse clicks
def on_click(event):
    label.config(text=f"Mouse clicked at ({event.x}, {event.y})")

# Function to handle key presses
def on_key(event):
    label.config(text=f"Key pressed: {event.char}")

# Bind events
root.bind("<Button-1>", on_click)  # Left mouse click
root.bind("<Key>", on_key)         # Any key press

root.mainloop()
