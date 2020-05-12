from tkinter import *
from tkinter import messagebox as ms
root=Tk()
def Left_Click(event):
    ms.showinfo("Message","Left Click of mouse is pressed")
def Right_Click(event):
    ms.showinfo("Message","Right Click of mouse is pressed")
def Scroll(event):
    ms.showinfo("Message","Scroll of mouse is pressed")
def Left_Arrow(event):
    ms.showinfo("Message","Left Arrow Button of Keyboard is pressed")
def Right_Arrow(event):
    ms.showinfo("Message","Right Arrow Button of Keyboard is pressed")
root.bind("<Button-1>",Left_Click)
root.bind("<Button-3>",Right_Click)
root.bind("<Button-2>",Scroll)
root.bind("<Left>",Left_Arrow)
root.bind("<Right>",Right_Arrow)
root.mainloop()
