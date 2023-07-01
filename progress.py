from tkinter import *
from tkinter.ttk import *
import subprocess
import tkinter as tk

def home1():
    subprocess.call(["python", "home.py"])

def bar():
    import time
    for i in range(1,101,1):
        progress['value'] = i
        root.update_idletasks()
        lb.config(text="Loading "+str(i)+"%")
        time.sleep(0.01)

    progress['value'] = 100
    home1()
    root.destroy()



root = Tk()
#===============================backckground image=====================================================================
canvas= tk.Canvas(width=1600, height=600,background='white')
canvas.pack(expand=YES,fill=BOTH)
img=tk.PhotoImage(file="E://pythonProject//images//1.png")
canvas.create_image(15,10,image=img,anchor=NW)
#======================================================================================================================
f1 = "arial 15 bold"
lb = Label(root,text="",font=f1,background='white')
lb.place(x=585,y=270)
#=============================================


s = Style()
s.configure("TProgressbar", foreground='#09BF14', background='#09BF14', thickness=100)

progress = Progressbar(root,style="TProgressbar", length=700, mode='determinate')
progress.place(x=300,y=300)

#btn = Button(root, text='Click >>', command=bar)
#btn.place(x=600,y=340)
img1 = tk.PhotoImage(file="E://pythonProject//images//OIP (2)1.png")
b3 = tk.Button(root, image=img1,bd=0, bg="white", width=100, height=30,command=bar)
b3.place(x=590,y=340)


#root.geometry("710x150+200+200")
root.title("progress")
root.state('zoomed')
mainloop()