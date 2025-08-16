'''
✅ Concept:

pack() arranges widgets top, bottom, left, right of the parent window.

You can use options like side, fill, expand.
'''

import tkinter as tk

root = tk.Tk()
root.title("Pack Layout Demo")
root.geometry("300x200")

# Create labels with different background colors
lbl1 = tk.Label(root, text="Top", bg="lightblue")
lbl2 = tk.Label(root, text="Left", bg="lightgreen")
lbl3 = tk.Label(root, text="Right", bg="lightpink")
lbl4 = tk.Label(root, text="Bottom", bg="lightyellow")

# Pack them in different directions
lbl1.pack(side="top", fill="x")
lbl2.pack(side="left", fill="y")
lbl3.pack(side="right", fill="y")
lbl4.pack(side="bottom", fill="x")

root.mainloop()






'''
Explanation
side="top" → widget placed at the top.

fill="x" → fills horizontally.

fill="y" → fills vertically.

expand=True → widget expands to fill available space.
'''