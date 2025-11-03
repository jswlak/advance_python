from tkinter import *

root = Tk()
root.title("Digital Clock")
root.geometry("300x150")

#Label to Show Time
time_label = Label(root, text="00:00:00", font=("Helvetica", 48), fg="cyan", bg="black")
time_label.pack(expand=True, fill="both")



root.mainloop()
