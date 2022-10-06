# Show all employee

from tkinter import *
import csv
import os

def onscroll(axis, *args):
    if axis == 'y-axis':
        canvas.yview(*args)
    elif axis == 'x-axis':
        canvas.xview(*args)

global canvas
win1=Tk()
win1.title("EMS - Show all Employees")
win1_width=520
win1_height=360
win1_resolution=str(win1_width)+"x"+str(win1_height)
win1.geometry(win1_resolution)
win1.config(bg="orange")
win1.resizable(0,0)
if "nt" == os.name:
    win1.wm_iconbitmap("logo.ico")
else:
    win1.wm_iconbitmap("@logo.xbm")
frame=Frame(win1)
frame.pack()
yscrollbar = Scrollbar(frame, orient='vertical',command=lambda *args: onscroll('y-axis', *args))
yscrollbar.pack(side="right",anchor="w",fill="both")
canvas=Canvas(frame,bg="white",width=win1_width,height="300",scrollregion=(0, 0, 0, 2050),yscrollcommand=yscrollbar.set)
canvas.pack()
main_frame=Frame(canvas,bg="white")
canvas.create_window((0,0),window=main_frame,anchor="nw")
canvas.yview_scroll(100, "units")
canvas.xview_scroll(100, "units")
Label(main_frame,text="Emp. Code",bg="brown",fg="white",font=("Georgia",12)).grid(row=0,column=0)
Label(main_frame,text="Name",bg="brown",fg="white",font=("Georgia",12)).grid(row=0,column=1,padx=30)
Label(main_frame,text="Department",bg="brown",fg="white",font=("Georgia",12)).grid(row=0,column=2,padx=30)
Label(main_frame,text="Salary",bg="brown",fg="white",font=("Georgia",12)).grid(row=0,column=3,padx=30)
with open("records.csv") as file:
    read=csv.reader(file)
    row_value=1
    for i in read:
        Label(main_frame,text=i[0],bg="white",fg="brown",font=("Georgia",12)).grid(row=row_value,column=0)
        Label(main_frame,text=i[1],bg="white",fg="brown",font=("Georgia",12)).grid(row=row_value,column=1)
        Label(main_frame,text=i[2],bg="white",fg="brown",font=("Georgia",12)).grid(row=row_value,column=2)
        Label(main_frame,text=i[3],bg="white",fg="brown",font=("Georgia",12)).grid(row=row_value,column=3)
        row_value+=1
win1.mainloop()
