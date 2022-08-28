from cProfile import label
from logging import PlaceHolder
import tkinter as tk
from tkinter import *
import time

root = tk.Tk()
root.title("Digital clock")
root.eval("tk::PlaceWindow . center")
root.resizable(0,0)
root.geometry("500x200")

lblClock = tk.Label(root,text = "",font=("raleway", 40))
lblClock.place(relx=0.5,rely=0.5,anchor=CENTER)

def clock():
   hh= time.strftime("%I")
   mm= time.strftime("%M")
   ss= time.strftime("%S")
   day=time.strftime("%A")
   ap=time.strftime("%p")
   lblClock.config(text= hh + ":" + mm +":" + ss + " " + ap)
   lblClock.after(500,clock)

clock()    

root.mainloop()