'''
✅ Concept:

grid() arranges widgets in a table-like structure (rows & columns).

Each widget is placed using row and column index.

Supports options like rowspan, columnspan, sticky.
'''

import tkinter as tk

root = tk.Tk()
root.title("Grid Layout Demo")
root.geometry("300x200")

# Create labels
lbl1 = tk.Label(root, text="Row 0, Col 0", bg="lightblue")
lbl2 = tk.Label(root, text="Row 0, Col 1", bg="lightgreen")
lbl3 = tk.Label(root, text="Row 1, Col 0", bg="lightpink")
lbl4 = tk.Label(root, text="Row 1, Col 1", bg="lightyellow")

# Place them in grid
lbl1.grid(row=0, column=0, padx=5, pady=5)
lbl2.grid(row=0, column=1, padx=5, pady=5)
lbl3.grid(row=1, column=0, padx=5, pady=5)
lbl4.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()






'''
Explanation

row=0, column=0 → top-left position.

padx, pady → add spacing around widgets.

sticky="nsew" → stick widget to North, South, East, West (fills cell).

columnspan=2 → widget spans across multiple columns.

'''

