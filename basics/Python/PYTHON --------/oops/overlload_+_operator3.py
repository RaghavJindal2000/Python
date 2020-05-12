class Sample:
    def __init__(self,x):
        self.x=x
    def __truediv__(self,other):
        m=self.x + other.x
        return m
obj1=Sample(100)
obj2=Sample(200)
#print(obj1.__truediv__(obj2))	
print(obj1/obj2)