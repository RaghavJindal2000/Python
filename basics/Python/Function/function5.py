def A():
    print("In A functon")
    B()
    print("Back to A")
def B():
    print("In B functon")
    C()
    print("Back to B")
def C():
    print("In C functon")
print("In Main Function")
A()
print("Back to Main")
input()
