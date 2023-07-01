from tkinter import PhotoImage, YES, BOTH, NW
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import datetime

# dictionary of colors:
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

# setting root window:
root = tk.Tk()
root.title("Home")
#root.config(bg="gray17")
#root.geometry("1250x600")
root.geometry("1920x1080+0+0")
root.state("zoomed")



#calling nav buttons
def prof():
    messagebox.showinfo("Profile","Name:Keerthi Prasad D L\nRegno:R2011053\nCourse:BCA\nSection:A\nYear:3rd year\nCollege:SDC College,Kolar")
def help():
    messagebox.showerror("Help","Currently unavailable")
def feed():
    messagebox.askquestion("Feedback","Is this useful")
def set():
    messagebox.showerror("Settings","Currently No Settings")
def abot():
    messagebox.showinfo("About","It is the project,which helps teacher to maintain student details,attendance,and internal marks with softcopy."
                                "\n\nFrontend : Python [PyCharm 2022.1.3]\n\nBackend  : Sqlite [DB Browser for SQLite Version 3.12.2] ")

def logout():
    answer=messagebox.askquestion("Logout","Do you really want to logout")
    if answer=='yes':
        root.destroy()


# calling student management code
def go():
    subprocess.call(["python", "internals mang.py"])
# calling attendance code
def run1():
    subprocess.call(["python","attendance.py"])
    #calling std management
def call():
    subprocess.call(["python","std manage.py"])

def cal():
    subprocess.call(["python", "simple calculator.py"])

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="E://pythonProject//images//2.png")
closeIcon = PhotoImage(file="E://pythonProject//images//3.png")

# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="green")
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = tk.Frame(root, bg=color["orange"])
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="Teacher Friendly Portal", font="Bahnschrift 20 bold", bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack()

canvas= tk.Canvas(width=1280, height=600,bg="red")
canvas.pack(expand=YES,fill=BOTH)
img=tk.PhotoImage(file="E://pythonProject//images//image_downloader_16689229883756.png")
canvas.create_image(15,10,image=img,anchor=NW)

#logout button
my_img6 = tk.PhotoImage(file="E://pythonProject//images//image_downloader_16596909846223.png")
b3 = tk.Button(root, image=my_img6, bd=1, bg="gray17", width=100, height=30,command=logout)
b3.place(x=1150,y=100)

# Main label text:
#brandLabel = tk.Label(root, text="Welcome 😉", font="System 30", bg="#1E592F", fg="black")
#brandLabel.place(x=520, y=100)
brandimg=tk.PhotoImage(file="E://pythonProject//images//welcome_PNG131.png")
brandLabel=tk.Label(root,image=brandimg,bg="purple")
brandLabel.place(x=490,y=100)

brandLabel1 = tk.Label(root, text="Presented with 🖤 KPS", font="System 20", bg="gray17", fg="yellow",pady=26,padx=19)
brandLabel1.place(x=789, y=527)

lab=tk.Label(root,text="Menu ✔",font="courier 25 bold",bg="#1E592F",fg="white").place(x=320,y=230)

my_img2 = tk.PhotoImage(file="E://pythonProject//images//90.png")
b3 = tk.Button(root, image=my_img2, bd=0, bg="white", width=100, height=100,command=run1)
b3.place(x=400,y=300)
ea=tk.Label(root,text=" e- Attendance ",font="android 10 bold",bg="cyan").place(x=401,y=405)

my_img3 = tk.PhotoImage(file="E://pythonProject//images//227-2271076(2).png")
b4 = tk.Button(root, image=my_img3, bd=0, bg="white", width=100, height=100,command=call)
b4.place(x=550,y=300)
smg=tk.Label(root,text="  Student info  ",font="android 10 bold",bg="cyan").place(x=551,y=405)

my_img1 = tk.PhotoImage(file="E://pythonProject//images//16853061.png")
b2 = tk.Button(root, image=my_img1, bd=0,bg="white", width=100, height=100,command=go)
b2.place(x=695,y=300)
ims=tk.Label(root,text=" Internal Marks",font="android 10 bold",bg="cyan").place(x=696,y=405)

my_img5 = tk.PhotoImage(file="E://pythonProject//images//R1.png")
b5 = tk.Button(root,image=my_img5,bd=0,bg='pink',width=73,height=80,command=cal)
b5.place(x=1150,y=170)
calcu=tk.Label(root,text="Calculator ",font="android 10 bold",bg="yellow").place(x=1150,y=252)

# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
navbarBtn.place(x=20, y=15)

# setting Navbar frame:
navRoot = tk.Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Developer Profile", "Settings", "Help", "About", "Feedback"]
# Navbar Option Buttons:
for i in range(1):
    tk.Button(navRoot, text=options[0], font="BahnschriftLight 15", bg="gray17", fg=color["orange"],
              activebackground="gray17", activeforeground="green", bd=0,command=prof).place(x=25, y=y)
    y += 40
    tk.Button(navRoot, text=options[1], font="BahnschriftLight 15", bg="gray17", fg=color["orange"],
              activebackground="gray17", activeforeground="green", bd=0,command=set).place(x=25, y=y)
    y += 40
    tk.Button(navRoot, text=options[2], font="BahnschriftLight 15", bg="gray17", fg=color["orange"],
              activebackground="gray17", activeforeground="green", bd=0,command=help).place(x=25, y=y)
    y += 40
    tk.Button(navRoot, text=options[3], font="BahnschriftLight 15", bg="gray17", fg=color["orange"],
              activebackground="gray17", activeforeground="green", bd=0,command=abot).place(x=25, y=y)
    y += 40
    tk.Button(navRoot, text=options[4], font="BahnschriftLight 15", bg="gray17", fg=color["orange"],
              activebackground="gray17", activeforeground="green", bd=0,command=feed).place(x=25, y=y)
    y += 40
# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=250, y=5)

# time
label = tk.Label(root, text="Time", font=("Comic Sans", 20, "bold"), bg="yellow")
label.place(x=1130, y=20)


while True:
    time = str(datetime.datetime.now().time())
    label.config(text=time[:-7])
    root.update()

# window in mainloop:
root.mainloop()