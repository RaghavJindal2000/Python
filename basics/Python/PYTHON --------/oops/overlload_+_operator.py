class Sample:
    def __init__(self,x=0):
        self.x=x
    def display(self):
        print(self.x)
    def __sub__(self,other):
        obj=Sample()
        obj.x=self.x + other.x
        return obj
obj1=Sample(30)
obj2=Sample(20)
obj3=obj1-obj2
obj3.display()



class Sample:
	def add(self):
		self.__a = 45
	def display(self):
		print(self.__a)

obj = Sample()
obj.add()
obj.display()	
print(obj.__a)	


class Sample:
	def __add(self):
		print("in add")
	def show(self):
		print("in show")
		self.__add()
obj = Sample()
obj.show()

class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")

for x in Shark(),Clownfish():
	x.swim()
	x.swim_backwards()
	x.skeleton()


class Sample:
	def add(self):
		self.a = 25
class Example(Sample):
	def __init__(self):
		print("in init")

obj = Sample()
obj.add()

isinstance(obj, Sample)			
issubclass(Example, Sample)		
getattr(obj, 'a')
setattr(obj, 'a', 55)
delattr(obj, 'a')

class Sample:
	def example(self):
		print("in example : ",self)
	class A:
		def abc(self):
			print("in abc : ",self)
obj = Sample.A()
obj.abc()



