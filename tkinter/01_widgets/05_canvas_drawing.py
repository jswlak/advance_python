import tkinter as tk

root = tk.Tk()
root.title("Canvas Demo")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Draw a rectangle
canvas.create_rectangle(50, 50, 150, 100, fill="blue")

# Draw text
canvas.create_text(100, 75, text="Company Logo", fill="white")

root.mainloop()






# Key Points:

# Canvas is for custom drawings (charts, shapes, images).

# .create_rectangle() and .create_text() are just examples.

