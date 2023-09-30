# Main file

from tkinter import *
import csv
import os

file=open("records.csv","a")
file.close()
def close():
    win.destroy()
def about():
    os.system("python about.py")
def showall():
    os.system("python showall.py")
def edit():
    os.system("python edit.py")
def delete():
    os.system("python delete.py")
def searchrec():
    os.system("python searchrec.py")
def addrec():
    os.system("python addrecord.py")
def mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
def onscroll(axis, *args):
    global canvas
    if axis == 'y-axis':
        canvas.yview(*args)
    else:
        assert False, f"axis {axis} is incorrect, use 'x-axis' or 'y-axis'"

win=Tk()
win.title("EMS")
win_width = 350
win_height = 480
win_resolution = str(win_width)+"x"+str(win_height)
win.geometry(win_resolution)
win.config(bg="orange")
win.resizable(0,0)
if "nt" == os.name:
    win.wm_iconbitmap("logo.ico")
else:
    win.wm_iconbitmap("@logo.xbm")
Label(win,text="Employee Management System",bg="brown",fg="white",font=("Georgia",16)).pack(pady=10)
b1=Button(win,text="Show all Records",bg="white",fg="brown",border=5,relief="raise",font=("Georgia",13),width=20,command=showall)
b2=Button(win,text="Add Record",bg="white",fg="brown",border=5,relief="raise",font=("Georgia",13),width=20,command=addrec)
b2.pack(pady=8)
b3=Button(win,text="Search Records",bg="white",fg="brown",border=5,relief="raise",font=("Georgia",13),width=20,command=searchrec)
b3.pack(pady=8)
b4=Button(win,text="Edit Record",bg="white",fg="brown",border=5,relief="raise",font=("Georgia",13),width=20,command=edit)
b4.pack(pady=8)
b5=Button(win,text="Delete Record",bg="white",fg="brown",border=5,relief="raise",font=("Georgia",13),width=20,command=delete)
b5.pack(pady=8)
b6=Button(win,text="About",bg="white",fg="brown",border=5,relief="raise",font=("Georgia",13),width=20,command=about)
b6.pack(pady=8)
b7=Button(win,text="Quit",bg="white",fg="brown",border=5,relief="raise",font=("Georgia",13),width=20,command=close)
b7.pack(pady=8)
win.mainloop()
