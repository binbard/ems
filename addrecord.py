﻿# Add new employee 

from tkinter import messagebox
from tkinter import *
import csv
import os

global ele
ele=[1,2,3,4]
counto=0
def add():
    eid=ele[0].get()
    name=ele[1].get()
    dept=ele[2].get()
    salary=ele[3].get()
    if eid=="" or name=="" or dept=="" or salary=="":
        messagebox.showinfo("CSV","Please fill all fields")
    else:
        file=open("records.csv","a")
        csv_writer = csv.writer(file,delimiter=",",lineterminator="\n")
        csv_writer.writerow([eid,name,dept,salary])
        ans=messagebox.askquestion("CSV","Record Added Sucessfully!\nWould you like to add another? ")
        if ans=="yes":
            win.destroy()
            file.close()
            main()
        else:
            win.destroy()
            file.close()

def press(e):
    global ele,counto
    if counto==len(ele)-1 and repr(e.keysym)=="'Return'":
        return add()
    if repr(e.keysym)=="'Down'" or repr(e.keysym)=="'Return'":
        if(counto!=len(ele)-1): counto+=1
    elif repr(e.keysym)=="'Up'":
        if(counto!=0): counto-=1
    ele[counto].focus()

def main():
    global ele,eid,name,salary,dept,win
    win=Tk()
    win.title("EMS - Add Employee")
    win.geometry("300x250")
    win.config(bg="orange")
    if "nt" == os.name:
     win.wm_iconbitmap("logo.ico")
    else:
     win.wm_iconbitmap("@logo.xbm")
    win.resizable(0,0)
    eid=StringVar()
    name=StringVar()
    dept=StringVar()
    salary=StringVar()
    Label(win,text="Add New Employee",bg="brown",fg="white",font=("Georgia",16)).place(x=60,y=2)
    Label(win,text="Emp. Code:",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=50)
    Label(win,text="Name:",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=90)
    Label(win,text="Department:",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=130)
    Label(win,text="Salary (in K):",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=170)
    ele[0]=Entry(win,textvariable=eid)
    ele[0].place(x=140,y=50)
    ele[1]=Entry(win,textvariable=name)
    ele[1].place(x=140,y=90)
    ele[2]=Entry(win,textvariable=dept)
    ele[2].place(x=140,y=130)
    ele[3]=Entry(win,textvariable=salary)
    ele[3].place(x=140,y=170)
    # ele[0].focus()
    Button(win,text="Add",bg="white",fg="brown",font=("Georgia",9),command=add).pack(anchor="s",side="bottom")
    win.bind("<Key>",press)
    win.mainloop()
if __name__=="__main__":
    main()
