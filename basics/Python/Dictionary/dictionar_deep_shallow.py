a={"Nitin":23,"Amit":21,"Rishabh":22}
print(a)
print(len(a))
b=a.copy()#DeepCopy
print(b)

b["Nitin"]=25
print("After Updation")
print(a)
print(b)

c=a#Shallow Copy
print(c)
c["Amit"]=23
print("After Updation")
print(a)
print(b)
print(c)
input()
