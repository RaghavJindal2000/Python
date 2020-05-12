from pymysql import *
class Student:
	def __init__(self):
		self.con=connect(db='batch',user='root',password='root',host='localhost')
		self.cur=self.con.cursor()
	def addstudent(self):
		id=int(input("Enter Id : "))
		name=input("Enter Name : ")
		address=input("Enter Address : ")
		self.cur.execute("INSERT into student values(%d,'%s','%s')"%(id,name,address))
		self.con.commit()
	def showdetail(self):
		self.cur.execute("select * from student")
		result=self.cur.fetchall()
		#print(result)
		
		print("==================================")
		print("ID\tName\tAddress")	
		print("==================================")
		for x in result:
			print("%d\t%s\t%s"%(x[0],x[1],x[2]))
		print("===================================")	
		
	def deletestudent(self):
		id = int(input("Enter Your ID :  "))
		self.cur.execute("delete from student where id = %d"%id)
		self.con.commit()
		print("Record Deleted.")
	
	def updatestudent(self):
		id = int(input("Enter Id : "))
		name = input("Enter Name  : ")
		address = input("Enter Address")
		self.cur.execute("update student set name='%s',address='%s' 
		where id = %d"%(name,address,id))
		self.con.commit()
a=Student()
while True:
	print("Press 1 to add\nPress 2 to show\nPress 3 to find\nPress 4 to update\nPress 5 to delete\nPress 6 to exit")
	c=int(input("Enter Your Choice :  "))
	if(c==1):
		a.addstudent()
	elif(c==2):
		a.showdetail()
	elif c==4:
		a.updatestudent()	
	elif c==5:
		a.deletestudent()
	elif(c==6):
		break
	else:
		print("Wrong Input")
a.con.close()		