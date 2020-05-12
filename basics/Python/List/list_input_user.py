print("Enter Item into List ")
try:
    a=[int(x) for x in input().split()]
    print("list is ",a)
except:
    print("Can't Convert String Litral into Integer")
input()
