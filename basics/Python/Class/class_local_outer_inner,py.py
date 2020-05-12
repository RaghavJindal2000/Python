class Outer:
    def display(self):
        print("In Display function of Outer Class")
        class Local:
            def show(self):
                print("In Show function of Local Class")
        ob=Local()
        ob.show()
    class Inner:
        def fun(self):
            print("In fun function of Inner Class")
x=Outer()
x.display()
y=Outer.Inner()
y.fun()
input()
