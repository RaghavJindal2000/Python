def display():
    global a
    a=a+1
    print(a,"In Display function")
    if(a<5):
        display()
    print(a,"Back to display")
a=0
print("In Main")
display()
print("Back to main")
