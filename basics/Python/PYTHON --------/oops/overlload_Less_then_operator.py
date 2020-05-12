class Sample:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        if(self.x>other.x):
            return True
        else:
            return False
obj1=Sample(10)
obj2=Sample(20)
if(obj1<obj2):
    print("obj1 is smaller")
else:
    print("obj2 is smaller")
