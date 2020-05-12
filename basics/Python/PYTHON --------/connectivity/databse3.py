from pymysql import *
import random
con=connect(db="Bank2",user="root",password="root",host="localhost")
cur=con.cursor()
def add():
	name=input("Enter the Name          :  ")
	age=int(input("Enter Your age : "))
	acc_no = random.randrange(111111,999999)
	cur.execute("insert into customer values('%s',%d,%d)"%(name,age,acc_no))
	con.commit()
	print("Data Inserted") 
def show():
	cur.execute("select * from customer")
	data = cur.fetchall()
	print("=================================")	
	print("Name\tAge\tAccount No.")	
	print("=================================")
	for x in data:
		print("%s\t%s\t%s"%(x[0],x[1],x[2]))
while True:
	print("Press 1 to add\nPress 2 to show\nPress 3 to Exit")
	c=int(input("Enter Your Choice : "))
	if c==1:
		add()
	elif c==2:
		show()
	elif c==3:
		break
	else:
		print("Invalid Choice")
con.close()