# Main file

from tkinter import *
import csv
import os

theme=0

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
def themeswitch():
    global theme
    if(theme==0):
        win.config(bg="#950101")
        Dark("")
        theme = 1
        win.update()
    else:
        win.config(bg="#08D9D6")
        Light("")
        theme=0
        win.update()
    

win=Tk()

def Light(self):
    b1=Button(win,text="Show all Records",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=showall)
    b2=Button(win,text="Add Record",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=addrec)
    b3=Button(win,text="Search Records",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=searchrec)
    b4=Button(win,text="Edit Record",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=edit)
    b5=Button(win,text="Delete Record",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=delete)
    b6=Button(win,text="About",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=about)
    b7=Button(win,text="Light/Dark Mode",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=themeswitch)
    b8=Button(win,text="Quit",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=close)
def Dark(self):
    b1=Button(win,text="Show all Records",bg="#B1B2FF",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=showall)
    b2=Button(win,text="Add Record",bg="#B1B2FF",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=addrec)
    b3=Button(win,text="Search Records",bg="#B1B2FF",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=searchrec)
    b4=Button(win,text="Edit Record",bg="#B1B2FF",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=edit)
    b5=Button(win,text="Delete Record",bg="#B1B2FF",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=delete)
    b6=Button(win,text="About",bg="#B1B2FF",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=about)
    b7=Button(win,text="Light/Dark Mode",bg="#B1B2FF",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=themeswitch)
    b8=Button(win,text="Quit",bg="#B1B2FF",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=close)
        

win.title("EMS")
win.geometry("350x550")
win.resizable(0,0)
if "nt" == os.name:
    win.wm_iconbitmap("logo.ico")
else:
    win.wm_iconbitmap("@logo.xbm")
win.config(bg="#08D9D6")
Label(win,text="Employee Management System",bg="#256D85",fg="#EAEAEA",font=("Georgia",16)).pack(pady=10)
b1=Button(win,text="Show all Records",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=showall)
b1.pack(pady=8)
b2=Button(win,text="Add Record",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=addrec)
b2.pack(pady=8)
b3=Button(win,text="Search Records",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=searchrec)
b3.pack(pady=8)
b4=Button(win,text="Edit Record",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=edit)
b4.pack(pady=8)
b5=Button(win,text="Delete Record",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=delete)
b5.pack(pady=8)
b6=Button(win,text="About",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=about)
b6.pack(pady=8)
b7=Button(win,text="Light/Dark Mode",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=themeswitch)
b7.pack(pady=8)
b8=Button(win,text="Quit",bg="#FF2E63",fg="#EAEAEA",border=5,relief="raise",font=("Georgia",13),width=20,command=close)
b8.pack(pady=8)
win.mainloop()
