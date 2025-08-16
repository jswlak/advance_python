'''
✅ Concept:

place() is used for absolute positioning.

You can set widgets by x, y coordinates or by relative position (relx, rely, relwidth, relheight).

Gives full control over exact widget placement.


'''

import tkinter as tk

root = tk.Tk()
root.title("Place Layout Demo")
root.geometry("300x200")

# Absolute positioning
lbl1 = tk.Label(root, text="(50, 50)", bg="lightblue")
lbl1.place(x=50, y=50)

lbl2 = tk.Label(root, text="(150, 100)", bg="lightgreen")
lbl2.place(x=150, y=100)

# Relative positioning (percentage of window size)
lbl3 = tk.Label(root, text="Center", bg="lightpink")
lbl3.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()






'''
Explanation


place(x=50, y=50) → puts widget at absolute coordinates.

relx=0.5, rely=0.5 → 50% from left, 50% from top (center).

anchor="center" → aligns the center of widget to the point.

relwidth=0.5, relheight=0.2 → widget takes % of window size.
'''