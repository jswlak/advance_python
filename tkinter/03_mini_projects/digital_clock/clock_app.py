from tkinter import *

import time

root = Tk()
root.title("Digital Clock")
root.geometry("400x200")

#Label to Show Time
time_label = Label(root, text="00:00:00", font=("Helvetica", 48), fg="cyan", bg="black")
time_label.pack(expand=True, fill="both")

#add style
root.configure(bg="black")
time_label.config(fg="lime", font=("Courier", 48, "bold"))

#date
date_label = Label(root, text="", font=("Helvetica", 18), fg="white", bg="black")
date_label.pack(side="bottom", fill="x")

#Fetch Current Time
# current_time = time.strftime("%H:%M:%S")
# print(current_time)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y") #current date
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)  # recall function every second

update_time()

root.mainloop()
