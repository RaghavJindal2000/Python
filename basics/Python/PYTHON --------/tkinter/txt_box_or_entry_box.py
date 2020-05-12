from tkinter import *
root=Tk()
l=Label(root,text="Mail : ")
l2=Label(root,text="Password : ")

txt1=Entry()
txt2=Entry()

l.grid(row=0,column=0)
txt1.grid(row=0,column=1)

l2.grid(row=1,column=0)
txt2.grid(row=1,column=1)

root.mainloop()
