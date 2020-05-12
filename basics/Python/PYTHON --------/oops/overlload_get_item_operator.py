class Sample:
    def __init__(self,a):
        self.a=a#[]
    def __getitem__(self,i):#i=0
        return self.a[i]#0
x=[10,20,30,40,50,60,70,80,90,100]
obj=Sample(x)
print("List Using Object is :  ")
for i in range(0,10):
    print(obj[i],end=" ")#obj[0]