class Sample:
	def __get(self):
		print(self)
		self.a=int(input())
		self.b=int(input())
class Example(Sample):
	def display(self):
		print(self)
		sum=self.a+self.b
		print("Sum  = ",sum)
obj=Example()
obj.get()
obj.display()

