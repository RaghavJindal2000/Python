#compare two list
a=[1,2,3,4]#a==b
b=[1,2,3,4]
f=0
i=0
while(i<len(a)):#3<3
	if(a[i]!=b[i]):#(a[2]!=b[2]) 1!=1
		f=1
		break
	i=i+1#i=3
if(f==0 and len(a)==len(b)):
	print("Both List are Same")
else:
	print("Both List are not same")
