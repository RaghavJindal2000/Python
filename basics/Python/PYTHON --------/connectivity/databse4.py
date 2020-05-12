from pymysql import *
con=connect(db="student",user="root",password="root",host="localhost")
cur=con.cursor()
def add():	
	id=int(input("Enter the Id of student : "))	
	name=input("Enter name :  ")
	amount = int(input("Enter Amount : "))
	cur.execute("insert into register values(%d,'%s',%d)"%(id,name,amount))
	con.commit()
def show():
	cur.execute("select * from register")
	result=cur.fetchall()
	for x in result:
		print("Id : ",x[0])
		print("Name : ",x[1])
		print("Amount : ",x[2])
#	print("===========================")
#	print("ID\tName\tAmount")
#	print("===========================")
#	for x in result:
#		print("%d\t%s\t%d"%(x[0],x[1],x[2]))
def search():
	id = int(input("Enter ID : "))
	cur.execute("select * from register where id = %d "%id)
	result = cur.fetchone()
	print(result)	
def update():
	id = int(input("Enter ID : "))
	amount = int(input("Enter Amount : "))
	cur.execute("update register set amount = %d where id = %d"%(amount,id))	
	con.commit()
def delete():
    id=int(input("Enter the Id to Delete "))
    cur.execute("delete from register where id = %d"%(id))
    con.commit()
    print("Record Deleted")
   
while True:
	print("Press 1 to add\n Press 2 for show\n Press 3 to Search\n Press 4 For update\nPress 5 for Delete\n Press 6 for exit")
	ch = int(input("Enter Your Choice : "))
	if ch == 1:
		add()
	elif ch == 2:
		show()
	elif ch==3:
		search()
	elif ch == 4:
		update()
	elif ch == 5:
		delete()
	elif ch == 6:
		break
	else:
		print("Wrong Input")
con.close()