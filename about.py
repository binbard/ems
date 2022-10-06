# About program - credits

from tkinter import *
import random
import os

colors=["red","blue","green"]
def click():
    cur_time=("©EMS\nContribute@Github \nMade with ❤️")
    label.config(text=cur_time,fg=random.choice(colors))
    label.after(1000,click)
win=Tk()
win.title("EMS - About")
win.config(bg="white")
win.resizable(0,0)
if "nt" == os.name:
    win.wm_iconbitmap("logo1.ico")
else:
    win.wm_iconbitmap("@logo1.xbm")
win.geometry("350x200")
label=Label(win,font=('Segoe Print',14,'bold'),bg='white')
label.pack()
click()
win.mainloop()
