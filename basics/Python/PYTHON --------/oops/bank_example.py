import random as rd
class Bank:
	def add(self):
		self.name=input("Enter Your Name  : ")
		self.age=int(input("Enter Age  : "))
		self.phone=int(input("Enter Phone : "))
		self.address=input("Enter Address  : ")
		self.pin=int(input("Enter Pin  : "))
		self.balance=int(input("Enter Amount  : "))
		self.account_number=rd.randrange(111111,999999)
	def deposit(self,amount=0):
		self.balance+=amount
		print("Your New Balance  : ",self.balance)
	def withdrawl(self,amount=0):
		if(amount<=self.balance):
			self.balance-=amount
			print("Remaining Balance : ",self.balance)
		else:
			print("Low Balance : ",self.balance)		
	def show_detail(self):
		print("Name : ",self.name)
		print("Age : ",self.age)
		print("Phone : ",self.phone)
		print("Address : ",self.address)
		print("PIN : ",self.pin)
		print("Balance : ",self.balance)
		print("Account Number : ",self.account_number)