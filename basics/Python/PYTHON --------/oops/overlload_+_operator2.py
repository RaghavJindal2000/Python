class Sample:
    def __init__(self,x=0,y=0):
        self.x=x#100  200 
        self.y=y#10   20
    def display(self):
        print(self.x,"\t",self.y)        
    def __add__(self,other):
        obj=Sample()
        obj.x=self.x * other.x
        obj.y=self.y - other.y
        return obj
obj1=Sample(2,6)
obj2=Sample(3,2)
obj3=Sample()
#obj3=obj1+obj2
obj3=obj2.__add__(obj1)
obj3.display()