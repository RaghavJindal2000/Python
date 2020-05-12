from tkinter import *
from tkinter import messagebox as ms
root=Tk()
rt=Tk()
def fun1():
    ms.showinfo("Button1","Hello World")
def fun2():
    ms.showinfo("Button2","Python is a great Language")
def fun3():
    ms.showinfo("Button3","Python is Developed by Guido Van Rossum")
def fun4():
    ms.showinfo("Button4","Python is a Pure Object Oriented Programming Language")
b1=Button(rt,text="This My Button One",command=fun1)
b2=Button(root,text="This My Button Two",bg="SkyBlue",command=fun2)
b3=Button(rt,text="This My Button Three",bg="Yellow",fg="Red",command=fun3)
b4=Button(root,text="This My Button Four",bg="Red",command=fun4)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)
root.mainloop()
