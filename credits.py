# © Harshit Jawla

from tkinter import*
from tkinter import messagebox
import os, random

colors=["red","blue","green"]
def click():
    cur_time=("©Harshit Jawla\n@Github")
    label.config(text=cur_time,fg=random.choice(colors))
    label.after(1000,click)
win=Tk()
win.title("EMS - Credits")
win.config(bg="white")
win.resizable(0,0)
win.iconbitmap("logo.ico")
win.geometry("200x60")
label=Label(win,font=('Segoe Print',14,'bold'),bg='white')
label.pack()
click()
win.mainloop()
