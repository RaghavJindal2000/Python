class Outer:
	def display(self):
		print(self)
		print("In display function of Outer class")
		class Local:
			def show(self):
				print("In Show function of Local Class")
		AB=Local()
		print(AB)
		AB.show()
	class Inner:
		def print_value(self):
			print("In Print_Value function of Inner Class")
obj=Outer()
obj.display()
print(dir(obj))
a=Outer.Inner()
#	a.show()
a.print_value()