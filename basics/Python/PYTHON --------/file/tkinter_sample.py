from tkinter import *
from tkinter import messagebox as m
root=Tk()
root.geometry("250x125")
root.title("Registration form")
def output():
	m.showinfo('message',"Thank You")
a=Label(root,text='First Name : ')
e=Entry(root)
e.grid(row=0,column=1)
a.grid(row=0,column=0)
a=Label(root,text='Last Name : ')
e1=Entry(root)
e1.grid(row=1,column=1)
a.grid(row=1,column=0)
b=Button(root,text="Submit",command=output)
b.grid(row=2,column=1)
root.mainloop()