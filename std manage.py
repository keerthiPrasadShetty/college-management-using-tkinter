from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Student.db")
root = Tk()
root.title("Student Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Student Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lbldoj = Label(entries_frame, text="D.O.B", font=("Calibri", 16), bg="#535c68", fg="white")
lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtDoj = Entry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30)
txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Father Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

txtAddress = Text(entries_frame, width=85, height=1, font=("Calibri", 16))
txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_student():
#===============================================validation=============================================================
    special_ch=['/','-']
    special_ch1 = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[',
                      ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']
#======================================================================================================================
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return False
    elif any(ch.isdigit() for ch in txtName.get()):
        messagebox.showwarning('Warninng', 'Name cannot have numbers')
        return False
    elif len(txtName.get()) <= 4 or len(txtName.get()) >= 25:
        messagebox.showwarning('Warning', 'Name is too short/long')
        return False
    elif not any(ch.isupper() for ch in txtName.get()):
        messagebox.showwarning('Name Warning', 'Enter Name starting with uppercase letter!')
        return False
    elif any(ch in special_ch1 for ch in txtName.get()):
        messagebox.showwarning('Name Warning', 'Special character not allowed')
        return False
    elif any(ch.isalpha() for ch in txtAge.get()):
        messagebox.showwarning('Warning', 'Age cannot have alphabets')
        return False
    elif len(txtAge.get()) < 0 or len(txtAge.get()) > 3:
        messagebox.showwarning('Warning', 'Enter proper age !!!')
        return False
    elif any(ch.isalpha() for ch in txtDoj.get()):
        messagebox.showwarning('Warning', 'DOB cannot have alphabets')
        return False
    elif not any(ch in special_ch for ch in txtDoj.get()):
        messagebox.showwarning('D.O.B Warning', 'Enter valid DOB!')
        return False
    elif len(txtContact.get()) < 10 or len(txtContact.get()) > 10:
        messagebox.showwarning('Warning', 'Enter only 10 digit phone number.')
        return False
    elif any(ch.isalpha() for ch in txtContact.get()):
        messagebox.showwarning('Warning', 'Phone number cannot have alphabets')
        return False
    elif any(ch.isdigit() for ch in txtEmail.get()):
        messagebox.showwarning('Warninng', 'Father Name cannot have no')
        return False
    elif len(txtEmail.get()) <= 4 or len(txtEmail.get()) >= 25:
        messagebox.showwarning('Warning', 'Father Name is too short/long')
        return False
    elif len(txtDoj.get()) < 10 or len(txtDoj.get())>10 :
        messagebox.showwarning('Warning', 'Enter valid DOB format')
        return False
    else:
        print("true")
#======================================================================================================================

    db.insert(txtName.get(),txtAge.get(), txtDoj.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtAddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Student Record Inserted Successfully")
    clearAll()
    dispalyAll()
#======================================================================================================================


#======================================================================================================================
def update_student():
    special_ch = ['/', '-']
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return False
    elif any(ch.isdigit() for ch in txtName.get()):
        messagebox.showwarning('Warninng', 'Name cannot have number')
        return False
    elif len(txtName.get()) <= 4 or len(txtName.get()) >= 25:
        messagebox.showwarning('Warning', 'Name is too short/long')
        return False
    elif not any(ch.isupper() for ch in txtName.get()):
        messagebox.showwarning('Name Warning', 'Enter Name starting with uppercase letter!')
        return False
    elif any(ch.isalpha() for ch in txtAge.get()):
        messagebox.showwarning('Warning', 'Age cannot have alphabets')
        return False
    elif len(txtAge.get()) < 0 or len(txtAge.get()) > 3:
        messagebox.showwarning('Warning', 'Enter proper age !!!')
        return False
    elif any(ch.isalpha() for ch in txtDoj.get()):
        messagebox.showwarning('Warning', 'DOB cannot have alphabets')
        return False
    elif not any(ch in special_ch for ch in txtDoj.get()):
        messagebox.showwarning('D.O.B Warning', 'Enter valid DOB!')
        return False
    elif len(txtContact.get()) < 10 or len(txtContact.get()) > 10:
        messagebox.showwarning('Warning', 'Enter only 10 digit phone number.')
        return False
    elif any(ch.isalpha() for ch in txtContact.get()):
        messagebox.showwarning('Warning', 'Phone number cannot have alphabets')
        return False
    elif any(ch.isdigit() for ch in txtEmail.get()):
        messagebox.showwarning('Warninng', 'Father Name cannot have no')
        return False
    elif len(txtEmail.get()) <= 4 or len(txtEmail.get()) >= 25:
        messagebox.showwarning('Warning', 'Father Name is too short/long')
        return False
    elif len(txtDoj.get()) < 10 or len(txtDoj.get())>10 :
        messagebox.showwarning('Warning', 'Enter valid DOB format')
        return False
    else:
        print("true")
    # ======================
    db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              txtAddress.get(
                  1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_student():
    db.remove(row[0])
    messagebox.askyesno("Confirm","Do you want to delete this record !!!")
    clearAll()
    dispalyAll()
    messagebox.showinfo("successful","successfully deleted record")


def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0, END)


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_student, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_student, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_student, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=380, width=1280, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1",width=-50)
tv.heading("2", text="Name")
tv.column("2", width=40)
tv.heading("3", text="Age")
tv.column("3", width=-50)
tv.heading("4", text="D.O.B")
tv.column("4", width=5)
tv.heading("5", text="Father Name")
tv.heading("6", text="Gender")
tv.column("6", width=-40)
tv.heading("7", text="Contact")
tv.column("7", width=3)
tv.heading("8", text="Address")
tv.column("8", width=5)

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
