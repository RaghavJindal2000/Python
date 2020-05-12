from tkinter import *
r = Tk()
r.title("Demo")
r.geometry("500x500")
r.configure(bg="white")

def sample():
    #print("Hello world")
    print("Hello",e1.get())

l = Label(r,text="Registration Page",
           font=('bold',30),
           bg="white")
l1 = Label(r,text="ID : ",font=('bold',20),bg="white")
l2 = Label(r,text="Name : ",font=('bold',20),bg="white")
l3 = Label(r,text="Age : ",font=('bold',20),bg="white")

e1 = Entry(r,font=("bold",15))
e2 = Entry(r,font=("bold",15))
e3 = Entry(r,font=("bold",15))

b1 = Button(text="Submit",
            font=("bold",15),
            bg="white",
            activebackground="white",
            activeforeground="red",
            borderwidth=0,
            command=sample)

l.place(x=100,y=40)
l1.place(x=110,y=100)
l2.place(x=110,y=140)
l3.place(x=110,y=180)

e1.place(x=220,y=107)
e2.place(x=220,y=147)
e3.place(x=220,y=187)

b1.place(x=280,y=240)

r.mainloop()