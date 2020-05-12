class Sample:
    def display(self,x):
        print("In Display function With 1 Param")
    def display(self,x,y):
        print("In Display function With 2 Param")
    def display(self):
        print("In Display function With 0 Param")
ob=Sample()
ob.display()
input()
