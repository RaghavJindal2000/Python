class Add:
    def get(self):
        self.__a=int(input("Enter the First Numbers : "))
        self.__b=int(input("Enter the First Numbers : "))
        self.__s=self.__a+self.__b
    def display(self):
        print("Sum = ",self.__s)
x=Add()
x.get()
x.display()
#print(x.__s)#show an Error
input()
