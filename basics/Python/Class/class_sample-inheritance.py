class Sample:
    def display(self):
        print("In display function of sample")
class Example(Sample):
    def show(self):
        print("In show function of sample")
obj=Example()
obj.display()
obj.show()
input()
