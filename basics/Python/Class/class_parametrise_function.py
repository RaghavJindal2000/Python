class Add:
    def get(self,x,y):
        self.__a=x
        self.__b=y
        self.__s=self.__a+self.__b
    def display(self):
        print("Sum = ",self.__s)
x=Add()
x.get(10,20)
x.display()
#print(x.__s)#show an Error
input()
