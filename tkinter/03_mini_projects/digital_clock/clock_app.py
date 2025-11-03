from tkinter import *

import time

root = Tk()
root.title("Digital Clock")
root.geometry("300x150")

#Label to Show Time
time_label = Label(root, text="00:00:00", font=("Helvetica", 48), fg="cyan", bg="black")
time_label.pack(expand=True, fill="both")


#Fetch Current Time
# current_time = time.strftime("%H:%M:%S")
# print(current_time)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # recall function every second

update_time()

root.mainloop()
