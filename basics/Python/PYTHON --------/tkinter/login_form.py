from tkinter import *
from tkinter import messagebox as ms
import os
root=Tk()
def submit():
    ms.showinfo("Submit","Welcome")
def cancel():
	ms.showinfo("Cancel","Bye Bye!!!")
	root.destroy()
	os.system("py login_form.py")
lb=Label(root,text="Login")
lb.grid(row=0,column=0,columnspan=2)
l=Label(root,text="Mail")
l2=Label(root,text="Password")
txt1=Entry()
txt2=Entry()
l.grid(row=1,column=0,stick="W")
txt1.grid(row=1,column=1)
l2.grid(row=2,column=0)
txt2.grid(row=2,column=1,stick="W")
check=Checkbutton(root,text="Remember Password")
check.grid(columnspan=2)
b1=Button(root,text="Submit",command=submit)
b2=Button(root,text="Cancel",command=cancel)
b1.grid(row=4,column=1,stick="W")
b2.grid(row=4,column=2,stick="E")
root.mainloop()
