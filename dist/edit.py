# Edit employee details

import tkinter as tk
from tkinter import *
import csv
import os

global eid,name,dept,salary,win
def update():
    global eid,name,dept,salary,win
    u=eid.get()
    n=name.get()
    d=dept.get()
    s=salary.get()
    data=[]
    file=open("records.csv")
    read=csv.reader(file,delimiter=",")
    for row in read:
        if row[0]==u:
            data.append([row[0],n,d,s])
        else:
            data.append(row)
    file.close()
    file=open("records.csv","w")
    write=csv.writer(file,delimiter=",",lineterminator="\n")
    write.writerows(data)
    file.close()
    messagebox.showinfo("CSV","Data has been updated sucessfully!")
    win.geometry("350x80")
    eid.set("Select Emp. Code")
def find():
    global eid,name,dept,salary
    u=eid.get()
    if u=="Select Emp. Code":
        messagebox.showinfo("CSV","Please Select Emp. Code")
    elif len(u)>0 :
        file=open("records.csv")
        reader=csv.reader(file,delimiter=",")
        for row in reader:
            if str(u)==str(row[0]):
                win_width=400
                win_height=250
                win_resolution=str(win_width)+"x"+str(win_height)
                win.geometry(win_resolution)
                name.set(row[1])
                dept.set(row[2])
                salary.set(row[3])
        file.close()
def press(e):
    global eid,name,dept,salary
    u=eid.get()
    if u=="Select Emp. Code":
        messagebox.showinfo("CSV","Please Select Emp. Code")
    if repr(e.keycode)==67:
        close()
    elif len(u)>0 :
        if repr(e.keysym)=="'Return'":
            find()
    else:
        messagebox.showinfo("CSV","Please Select Emp. Code")
def main():
    global eid,name,dept,salary,win
    win=Tk()
    win.title("EMS - Edit Record")
    win_height=80
    win_width=400
    win_resolution=str(win_width)+"x"+str(win_height)
    win.geometry(win_resolution)
    win.config(bg="orange")
    win.resizable(0,0)
    image = tk.Image('photo',file ='logo.gif')
    if "nt" == os.name:
       win.tk.call('wm','iconphoto',win._w,image)
    else:
        win.wm_iconbitmap("@logo.xbm")
    eid=StringVar()
    name=StringVar()
    dept=StringVar()
    salary=StringVar()
    data=[]
    Label(win,text="Edit Record",bg="brown",fg="white",font=("Georgia",16)).place(x=120,y=2)
    Label(win,text="Emp. Code",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=50)
    Label(win,text="Name",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=90)
    Label(win,text="Department",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=130)
    Label(win,text="Salary",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=170)
    file=open("records.csv")
    read=csv.reader(file,delimiter=",")
    for row in read:
        data.append(row[0])
    e0=tk.OptionMenu(win,eid,"Select Emp. Code",*data)
    e0.place(x=140,y=50)
    e0.focus()
    e1=Entry(win,textvariable=name,state="normal")
    e1.place(x=140,y=90)
    e1.focus()
    e2=Entry(win,textvariable=dept,state="normal")
    e2.place(x=140,y=130)
    e3=Entry(win,textvariable=salary,state="normal")
    e3.place(x=140,y=170)
    Button(win,text="Find",bg="white",fg="brown",font=("Georgia",9),command=find).place(x=320,y=50)
    Button(win,text="Update",bg="white",fg="brown",font=("Georgia",9),command=update).place(x=150,y=200)
    win.bind("<Key>",press)
    win.mainloop()
if __name__=="__main__":
    main()
