from tkinter import *
from tkinter import messagebox as ms
def fun1():
	ms.showinfo("Button1","Hello World")
def fun2():
    ms.showinfo("Button2","Python is a Great Language")
def fun3():
    ms.showinfo("Button3","Python is Developed by Guido Van Rossum")
root=Tk()
b1=Button(text="This My Button One",command=fun1)
b2=Button(text="This My Button Two",bg="SkyBlue",command=fun2)
b3=Button(text="This My Button Three",bg="Yellow",fg="Red",command=fun3)
b1.grid()
b2.grid()
b3.grid()
root.mainloop()
