str=input("Enter the String ")#Hello python world
length=len(str)#11
print("original String is :  ")
print(str)
s=""
for i in range(length-1,-1,-1):#(10,-1,-1) i=0
	if(i==0 or str[i-1]==" "): #str[5]=" "
		for j in range(i,length):#(0,11) j=5
			if(str[j]==" "):
				break
			else:
				s=s+str[j]#"world Hello"
		s=s+" "#"world "		
print("String in Reverse Order :  ")
print(s)