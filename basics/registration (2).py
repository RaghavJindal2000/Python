from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import sys

con = sqlite3.connect("register.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS `register` (`fname` TEXT NOT NULL,`lname` TEXT NOT NULL,`uname` TEXT NOT NULL,`email` TEXT NOT NULL,`password` INTEGER NOT NULL,PRIMARY KEY(`uname`,`email`));")  
root = Tk()
f1 = Frame(root)
f1.pack()
root.geometry('500x500')
root.title("Bank APP")




def check():
	try:	
		cur.execute("select * from register where uname = '%s' and password = %d"%(entry_11.get(),int(entry_12.get())))
		data = cur.fetchone()
		if data is not None:
			label_13=Label(f2,text=f"Hello {data[0]} {data[1]}",width=20,font=("bold",15))
			label_13.pack()
		else:	
			ms.showerror("Error","This Username And PassWord is not Registerd")	
	except:
		ms.showerror("Error",str(sys.exc_info()[1]))
			
		
def login():
	print("Hello World")
	global entry_11,entry_12,f2
	f1.destroy()
	f2 = Frame(root)
	label_9=Label(f2,text="Login Form",width=20,font=("bold",20))
	label_9.pack()
	label_10=Label(f2,text="UserName : ",width=20,font=("bold",10))
	label_10.pack()
	entry_11=Entry(f2)
	entry_11.pack()
	label_12=Label(f2,text="PassWord : ",width=20,font=("bold",10))
	label_12.pack()
	entry_12=Entry(f2)
	entry_12.pack()
	b3  = Button(f2,text="Login", width=20, command=check)
	b3.pack()
	f2.pack()

def register():
	try:
		cur.execute("insert into register values ('%s','%s','%s','%s',%d)"%(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),int(entry_5.get())))
		con.commit()
		ms.showinfo("Sumbit","Your Data is Registered")
		login()
	except sqlite3.IntegrityError as ie:
		ms.showerror("Error","Please Give Unique UserName and Email")
		entry_4.delete(0,'end')
		entry_5.delete(0,'end')
		return
	except ValueError as ve:
		ms.showerror("Error",ve)
		return
	

		
		
	

label_0=Label(f1,text="Registration Form",width=20,font=("bold",20))
label_0.pack()
label_1=Label(f1,text="First Name",width=20,font=("bold",10))
label_1.pack()
entry_1=Entry(f1)
entry_1.pack()
label_2=Label(f1,text="Last Name",width=20,font=("bold",10))
label_2.pack()
entry_2=Entry(f1)
entry_2.pack()
label_3=Label(f1,text="User Name",width=20,font=("bold",10))
label_3.pack()
entry_3=Entry(f1)
entry_3.pack()
label_4=Label(f1,text="Email",width=20,font=("bold",10))
label_4.pack()
entry_4=Entry(f1)
entry_4.pack()
label_5=Label(f1,text="Password",width=20,font=("bold",10))
label_5.pack()
entry_5=Entry(f1,show="*")
entry_5.pack()
b1=Button(f1,text='Submit',width=20,bg='brown',fg='white',command=register)
b1.pack()
b2=Button(f1,text='Login',width=20,bg='brown',fg='white',command=login)
b2.pack()
root.mainloop()