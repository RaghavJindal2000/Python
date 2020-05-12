from tkinter import *
from tkinter import messagebox as ms
root=Tk()
def display(event):
    s=txt.get()
    result.configure(text="Result : "+str(eval(s)))
l=Label(root,text="Enter Your Expression : ")
l.pack()
txt=Entry(root)
txt.bind("<Return>",display)
txt.pack()
result=Label(root)
result.pack()
root.mainloop()
