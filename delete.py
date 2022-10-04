# Delete records

from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import csv

global eid,name,dept,salary,win
def delete():
    global eid,name,dept,salary,win
    u=eid.get()
    n=name.get()
    c=dept.get()
    p=salary.get()
    data=[]
    file=open("records.csv")
    reader=csv.reader(file,delimiter=",")
    for row in reader:
        if row[0]==u:
            pass
        elif row[0]!=u:
            data.append([row[0],row[1],row[2],row[3]])
            
    file.close()
    file=open("records.csv","w")
    writer=csv.writer(file,delimiter=",",lineterminator="\n")
    writer.writerows(data)
    file.close()
    messagebox.showinfo("CSV","Record Deleted Sucessfully")
    ans=messagebox.askquestion("CSV","Record Deleted Sucessfully\nWant to Delete More ? ")
    if ans=="yes":
        win.destroy()
        file.close()
        main()
    else:
        win.destroy()
        file.close()
    #win.geometry("350x80")
    #eid.set("Select Emp. Code")
def find():
    global eid,name,dept,salary
    u=eid.get()
    if u=="Select Emp. Code":
        messagebox.showinfo("CSV","Please Select U.No.")
    elif len(u)>0 :
        file=open("records.csv")
        reader=csv.reader(file,delimiter=",")
        for row in reader:
            if u==row[0]:
                win.geometry("350x250")
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
    win.title("EMS - Delete Employee")
    win.geometry("350x80")
    win.config(bg="orange")
    win.resizable(0,0)
    win.iconbitmap("logo.ico")
    eid=StringVar()
    name=StringVar()
    dept=StringVar()
    salary=StringVar()
    data=[]
    Label(win,text="Delete Record",bg="brown",fg="white",font=("Georgia",16)).place(x=108,y=2)
    Label(win,text="Emp. Code",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=50)
    Label(win,text="Name",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=90)
    Label(win,text="Department",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=130)
    Label(win,text="Salary",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=170)
    file=open("records.csv")
    read=csv.reader(file,delimiter=",")
    for row in read:
        data.append(row[0])
    e0=ttk.OptionMenu(win,eid,"Select Emp. Code",*data)
    e0.place(x=140,y=50)
    e0.focus()
    e1=Entry(win,textvariable=name,state="disable")
    e1.place(x=140,y=90)
    e1.focus()
    e2=Entry(win,textvariable=dept,state="disable")
    e2.place(x=140,y=130)
    e3=Entry(win,textvariable=salary,state="disable")
    e3.place(x=140,y=170)
    Button(win,text="Find",bg="white",fg="brown",font=("Georgia",9),command=find).place(x=290,y=47)
    Button(win,text="Delete",bg="white",fg="brown",font=("Georgia",9),command=delete).place(x=150,y=200)
    win.bind("<Key>",press)
    win.mainloop()
if __name__=="__main__":
    main()
