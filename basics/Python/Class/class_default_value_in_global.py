class Sample:
    def get(self):
        global a
        a=0
    def display(self):
        print(a)
obj=Sample()
obj.get()
obj.display()
input()
