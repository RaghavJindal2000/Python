class Add:
    def get(self,x,y):
        global a,b,s
        a=x
        b=y
        s=a+b
    def display(self):
        print("Sum = ",s)
x=Add()
y=Add()
x.get(10,20)
x.display()
y.display
input()
