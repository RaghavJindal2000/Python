class Sample:
    def display(self):
        self.sum=self.a+self.b
        print("Sum = ",self.sum)
    def get(self):
        self.a=int(input("Enter a "))
        self.b=int(input("Enter b "))
    
class Example(Sample):
	def get(self):
		print("Welcome")
		super().get()
		self.display()
		print("Bye")
obj=Example()
obj.get()