#Searching:
#linear search
a=input("Enter String :  ")#hello
c=0
n=input("Enter the Charcater to count in String ")#l
for i in range(0,len(a)):#(0,5) i=0,1
	if(a[i]==n):#a[3]==l  l==l
		print(n," found at a[",i,"]")
		c=c+1#c=1+1=2
if(c==0):
	print(n," Does not Exist in List")
else:
	print("Total Result Found = ",c)
