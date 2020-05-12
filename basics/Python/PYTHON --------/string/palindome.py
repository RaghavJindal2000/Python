str=input("Enter the String :  ")#HIH
length=len(str)#3
f=0
for i in range(0,(int(length/2)+1)):#(0,2) i=1
	if(str[i] != str[length-1-i]):#(str[1]!= str[1] )
		f=1
		break
if(f==0):
	print("Palindomre")
else:
	print("Not Palindomre")
