class Base1():
    def get1(self):
        print("Enter the Two Numbers in Class Base1 :  ")
        self.a=int(input())
        self.b=int(input())
class Base2():
    def get2(self):
        print("Enter the Two Numbers in Class Base2 :  ")
        self.c=int(input())
        self.d=int(input())
class Derived(Base1,Base2):
    def display(self):
        sum=self.a+self.b+self.c+self.d
        print("Sum = ",sum)
obj=Derived()
obj.get1()
obj.get2()
obj.display()