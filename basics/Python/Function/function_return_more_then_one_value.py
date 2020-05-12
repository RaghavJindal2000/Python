def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y
a=10
b=20
print("Before Calling Swap a = ",a," and b = ",b)
a,b=swap(a,b)
print("After Calling Swap a = ",a," and b = ",b)
input()
