def display():
    global a
    a+=1
    print("In Display function")
    if(a<5):
        display()
    print("back to dislay")
a=0
print("In Main function")
display()
print("Back to Main function")
input()
