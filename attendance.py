from tkinter import *
import sqlite3
from tkinter import ttk,messagebox
from tkinter import PhotoImage, YES, BOTH, NW
import tkinter as tk


root = Tk()
root.geometry('630x410')
root.title("e-Attendance")

canvas= tk.Canvas(width=1280, height=600,bg="sky blue")
canvas.pack(expand=YES,fill=BOTH)
img=tk.PhotoImage(file="E://pythonProject//images//image_downloader_16689106229234.png")
canvas.create_image(15,10,image=img,anchor=NW)

Fullname = StringVar()
Date = StringVar()
var = IntVar()
c = StringVar()
#=========================================


def database():
    special_ch = ['/', '-']
    special_chh = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '{', '}', '[',
                   ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?']
    # =========================================
    name1 = Fullname.get()
    date = Date.get()
    status = var.get()
    course = c.get()
    conn = sqlite3.connect('Attendance.db')
    if name1=="" or date=="" or status=="" or course=="":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return False
    elif any(ch.isdigit() for ch in name1):
        messagebox.showwarning('Warninng', 'Name cannot have number')
        return False
    elif len(name1) <= 4 or len(name1) >= 25:
        messagebox.showwarning('Warning', 'Name is too short/long')
        return False
    elif any(ch.isalpha() for ch in date):
        messagebox.showwarning('Warning', 'DOB cannot have alphabets')
        return False
    elif any(ch in special_chh for ch in date):
        messagebox.showwarning('Warning', 'Enter Valid Characters only')
        return False
    elif not any(ch in special_ch for ch in date):
        messagebox.showwarning('Warning', 'Enter Valid Date')
        return False
    elif len(date) < 10 or len(date) > 10:
        messagebox.showwarning('Warning', 'Enter valid date')
        return False


    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Date TEXT,Status TEXT,course TEXT)')
    cursor.execute('INSERT INTO Student (FullName,Date,Status,course) VALUES(?,?,?,?)',
                   (name1, date, status, course,))
    conn.commit()
    messagebox.showinfo("info","Attendance Marked Successfully" )
    entry_1.delete(0, tk.END)


label_0 = Label(root, text="Daily Attendance System", width=20, font=("bold", 20))
label_0.place(x=250, y=40)

label_1 = Label(root, text="Full Name", width=10, font=("bold", 10))
label_1.place(x=250, y=130)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=420, y=130)

label_2 = Label(root, text="Date", width=10, font=("bold", 10))
label_2.place(x=250, y=180)


entry_2 =Entry(root, textvar=Date)
entry_2.place(x=420, y=180)

label_3 = Label(root, text="Status", width=10, font=("bold", 10))
label_3.place(x=250, y=230)

Radiobutton(root, text="Present", padx=5, variable=var, value=1).place(x=420, y=230)
Radiobutton(root, text="Absent", padx=20, variable=var, value=2).place(x=490, y=230)

label_4 = Label(root, text="Class", width=10, font=("bold", 10))
label_4.place(x=250, y=280)

list1 = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','SSLC','1st PU','2nd PU'];

droplist = OptionMenu(root, c, *list1)
droplist.config(width=15)
c.set('select Class')
droplist.place(x=420, y=280)


def view():
    lx = [Fullname.get(), "\t", Date.get(), "\t", var.get(), "\t", c.get()]
    messagebox.askyesno("Details", lx )


Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=250, y=340)
Button(root, text='Check', width=10, bg='blue', fg='white', command=view).place(x=400, y=340)
root.mainloop()