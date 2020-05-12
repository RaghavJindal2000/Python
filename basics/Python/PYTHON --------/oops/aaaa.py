class Sample:
	def __init__(self,x):
		self.x = x
	
	def __add__(self,other):
		print(self.x*other.x)
	
a=Sample(5)
b=Sample(10)
a+b