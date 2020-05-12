class Sample:
    def display(self):
        print("In Display function of Sample")
class Example(Sample):
    def display(self):
        super().display()
        print("In Display fuction of Example")
obj=Example()
obj.display()
input()
