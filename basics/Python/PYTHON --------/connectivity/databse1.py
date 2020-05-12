import sqlite3
class DBHelper():
	def __init__(self):
		self.conn=sqlite3.connect("sample.db")
		self.c=self.conn.cursor()
		self.c.execute("CREATE TABLE IF NOT EXISTS `student`(`id` INTEGER,`name` TEXT,`age` INTEGER,`gender` TEXT,PRIMARY KEY(`id`));")
	def add(self):
		id = int(input("Enter Id : "))
		name = input("Enter name : ")
		age = int(input("Enter Age : "))
		gender = input("Enter Gender : ")
		self.c.execute("insert into student values(%d,'%s',%d,'%s')" %(id,name,age,gender))
		self.conn.commit()
	def show(self):
		self.c.execute("select * from student")
		data = self.c.fetchall()
		print(data)
		
a=DBHelper()
a.add()
a.show()
a.conn.close()