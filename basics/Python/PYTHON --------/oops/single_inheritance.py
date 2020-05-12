class Sample:
    def display(self):
        print("In Base Class i.e. Sample Class")
class Example(Sample):
	def display(self):
		super().display()
		print("In Derived Class i.e. Example Class")
obj=Example()
obj.display()
