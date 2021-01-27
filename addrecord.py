# © Harshit Jawla

from tkinter import *
from tkinter import messagebox
import csv, os

counto=1
global e1,e2,e3,uno,name,clas,persent,win
def add():
    global e1,e2,e3,uno,name,clas,persent,win
    u=uno.get()
    n=name.get()
    c=clas.get()
    p=persent.get()
    if n=="" or c=="" or p=="":
        messagebox.showinfo("CSV","Please Fill All Feilds")
    else:
        file=open("records.csv","a")
        csv_writer = csv.writer(file,delimiter=",",lineterminator="\n")
        csv_writer.writerow([u,n,c,p])
        ans=messagebox.askquestion("CSV","Record Added Sucessfully\nWant to Add More ? ")
        if ans=="yes":
            win.destroy()
            file.close()
            main()
        else:
            win.destroy()
            file.close()
def press(e):
    global e1,e2,e3,uno,name,clas,persent,counto
    if counto==1 and repr(e.keysym)=="'Return'" or counto==1 and repr(e.keysym)=="'Down'":
        e2.focus()
        counto+=1
    elif counto==2 and repr(e.keysym)=="'Return'" or counto==2 and repr(e.keysym)=="'Down'":
        e3.focus()
        counto+=1
    elif  counto==3 and repr(e.keysym)=="'Return'":
        add()
        counto=3
    elif  counto==3 and repr(e.keysym)=="'Up'":
        e2.focus()
        counto-=1
    elif  counto==2 and repr(e.keysym)=="'Up'":
        e1.focus()
        counto=1
def main():
    global e1,e2,e3,uno,name,clas,persent,win
    win=Tk()
    win.title("EMS - Add Employee")
    win.geometry("300x250")
    win.config(bg="orange")
    win.iconbitmap("logo.ico")
    win.resizable(0,0)
    uno=StringVar()
    name=StringVar()
    clas=StringVar()
    persent=StringVar()
    Label(win,text="Add New Employee",bg="brown",fg="white",font=("Georgia",16)).place(x=60,y=2)
    Label(win,text="Emp. Code:",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=50)
    Label(win,text="Name:",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=90)
    Label(win,text="Department:",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=130)
    Label(win,text="Salary (in k):",bg="white",fg="brown",font=("Georgia",12)).place(x=30,y=170)
    e0=Entry(win,textvariable=uno)
    e0.place(x=140,y=50)
    e1=Entry(win,textvariable=name)
    e1.place(x=140,y=90)
    e1.focus()
    e2=Entry(win,textvariable=clas)
    e2.place(x=140,y=130)
    e3=Entry(win,textvariable=persent)
    e3.place(x=140,y=170)
    Button(win,text="Add",bg="white",fg="brown",font=("Georgia",9),command=add).pack(anchor="s",side="bottom")
    win.bind("<Key>",press)
    win.mainloop()
if __name__=="__main__":
    main()
