class Sample:
    def get(self,x):
        self.a=x
    def display(self):
        print(self.a)
    def __add__(self,other):
        t=Sample()
        t.a=self.a+other.a
        return t
ob1=Sample()
ob1.get(100)
ob2=Sample()
ob2.get(200)
ob3=Sample()
ob3=ob1+ob2
ob3.display()
input()
