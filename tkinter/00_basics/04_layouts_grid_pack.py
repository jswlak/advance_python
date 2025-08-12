import tkinter as tk

root = tk.Tk()
root.title("Layouts: pack() and grid()")
root.geometry("400x300")

# -------- PACK EXAMPLE --------
label1 = tk.Label(root, text="Pack Top", bg="lightblue")
label1.pack(side="top", fill="x", pady=5)

label2 = tk.Label(root, text="Pack Bottom", bg="lightgreen")
label2.pack(side="bottom", fill="x", pady=5)

label3 = tk.Label(root, text="Pack Left", bg="lightyellow")
label3.pack(side="left", fill="y", padx=5)

label4 = tk.Label(root, text="Pack Right", bg="lightpink")
label4.pack(side="right", fill="y", padx=5)


# -------- GRID EXAMPLE --------
grid_frame = tk.Frame(root, bg="white", relief="solid", bd=1)
grid_frame.pack(pady=20)

tk.Label(grid_frame, text="Row 0, Col 0", bg="#ddd").grid(row=0, column=0, padx=5, pady=5)
tk.Label(grid_frame, text="Row 0, Col 1", bg="#ccc").grid(row=0, column=1, padx=5, pady=5)
tk.Label(grid_frame, text="Row 1, Col 0", bg="#bbb").grid(row=1, column=0, padx=5, pady=5)
tk.Label(grid_frame, text="Row 1, Col 1", bg="#aaa").grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
