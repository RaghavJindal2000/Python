from tkinter import *
from tkinter import messagebox as ms
root=Tk()
def display():
	s=txt.get()
	print(s)
	ms.showinfo("Message","Hello "+s)
l=Label(root,text="Enter Your Name : ")
txt=Entry(root)
b1=Button(text="This My Button One",command=display)

l.grid(row=0,column=0)
txt.grid(row=0,column=1)
b1.grid(row=1,column=0)
root.mainloop()
