class ABCD:
	def __init__(self):
		self.a = int(input("Enter First Number: "))
		self.b = int(input("Enter Second Number: "))
	def display(self):
		print('sum : ',self.a+self.b)

obj=ABCD()
obj.display()