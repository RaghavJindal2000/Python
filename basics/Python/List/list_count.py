a=[10,20,30,40,10,10,10,30,30]
num=int(input("Enter the Item to Count "))
print(num," Exist ",a.count(num)," times")
print(num,"Exist at a[",a.index(num),"]")
for i in range(0,len(a)):
    if(a[i]==num):
        print(num," Exist at a[%d]"%i)
input()
