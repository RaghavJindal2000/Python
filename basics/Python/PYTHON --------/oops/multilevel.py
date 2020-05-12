class Base:
    def get(self):
        self.a=[25,8,12,1,8,4,2,1,21,54,51,2]
class Derived1(Base):
	def display(self):
		print(self.a)
class Derived2(Derived1):
    def sort(self):
        self.a.sort()
class Derived3(Derived2):
	def reverse(self):
		self.a.reverse()		
obj=Derived3()
obj.get()
print("Original List is :")
obj.display()	
obj.sort()
print("Sorted List is :")
obj.display()
obj.reverse()
print("Reversed List Is : ")
obj.display()