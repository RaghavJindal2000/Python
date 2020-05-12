from tkinter import *
root=Tk()
b1=Button(text="This My Button One")
b2=Button(text="This My Button Two",bg="SkyBlue")
b3=Button(text="This My Button Three",bg="Yellow",fg="Red")
b1.pack()
b2.pack(fill=X)
b3.pack(side=LEFT,fill=Y)
root.mainloop()
