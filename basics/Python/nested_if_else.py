print("Enter the Three Numbers : ")
a=int(input())
b=int(input())
c=int(input())
if(a<b):
    if(a<c):
        print(a," Is Smallest")
    else:
        print(c," Is Smallest")
else:
    if(b<c):
        print(b," Is Smallest")
    else:
        print(c," Is Smallest")
input()
