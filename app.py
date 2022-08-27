from cProfile import label
import tkinter as tk
import time



epoch_time = time.time()
local_time = time.ctime(epoch_time)

print("The local time is:", local_time)


root = tk.Tk()
root.title("Digital clock")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=600, height=300)
frame1.grid(row=0, column=0)



root.mainloop()