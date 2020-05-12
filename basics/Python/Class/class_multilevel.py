class Sample1:
    def __init__(self):
        print("In init block of sample1")
class Sample2(Sample1):
    def __init__(self):
        super().__init__()
        print("In init block of sample2")
class Example(Sample2):
    def __init__(self):
        super().__init__()
        print("In init block of example")
obj=Example()
input()
