class Sample:
    def __init__(self):
        print("In init block of sample")
class Example(Sample):
    def __init__(self):
        super().__init__()
        print("In init block of example")
obj=Example()
input()
