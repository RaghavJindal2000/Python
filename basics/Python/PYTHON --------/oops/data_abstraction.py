class Sample:
	def __init__(self,x=0,y=0):
		self.a=x
		self.b=y
	def display(self):
		print("add = ",self.a+self.b)
obj=Sample(y=8)
obj.display()