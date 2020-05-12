#GUI
#tkinter
from tkinter import *
import sqlite3

r = Tk()
r.title("Demo")
r.geometry("500x500")
r.configure(bg="white")

con = sqlite3.connect("form.db")
cur = con.cursor()
cur.execute("create table if not exists student(name text,age int);")

def sample():
    cur.execute("insert into student values('%s',%d)"%(e1.get(),int(e2.get())))
    con.commit()
    print("Registered")
    #l3= Label(text="Hello "+e1.get(),font=("bold",20),bg="white")
    #l3.place(x =100,y=150)
    #e1.delete(0,"end")

l = Label(r,text="Registration Form",font=('bold',20),bg="white",fg="blue") 
l1 = Label(r,text="Full Name : ",font=('bold',20),bg="white",fg="blue") 
e1 = Entry(r,bg="green",font=("bold",15))

l2 = Label(r,text="Age : ",font=('bold',20),bg="white",fg="blue") 
e2 = Entry(r,bg="green",font=("bold",15))

b1 = Button(r,text="Submit",
            font=("bold",10),
            bg="red",
            activebackground="green",
            width=10,
            command=sample)
#l1.pack(side="bottom")
l.place(x=140,y=50)
l1.place(x=60,y=100)
l2.place(x=60,y=150)
e1.place(x=230,y=107)
e2.place(x=230,y=150)

b1.place(x=260,y=200)
#l1.grid(row=5,column=0)
'''
pack-->side
place-->axis
grid-->row,column
'''

r.mainloop()
con.close()