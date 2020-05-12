'''
class Sample:
	a=5
	__b=25
	def add(self):
		print("in add")
		self.__show()
	def __show(self):
		print("in show",self.__b)

obj = Sample()
obj.add()		
print(obj.a)

class Car:
 
    __maxspeed = 0
    __name = ""
 
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
 
    def drive(self):
        print ('driving. maxspeed ' + str(self.__maxspeed))
 
redcar = Car()
redcar.drive()
redcar.__maxspeed = 10
redcar.drive()
'''
class Car:
 
    __maxspeed = 0
    __name = ""
 
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
 
    def drive(self):
        print ('driving. maxspeed ' + str(self.__maxspeed))
 
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed
 
redcar = Car()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()

