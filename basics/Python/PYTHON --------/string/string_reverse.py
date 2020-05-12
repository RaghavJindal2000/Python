str=input("Enter the String :  ")
print("Original String is = ",str)
s=""
for i in range(0,len(str)):
	s=str[i]+s
print("Reversed String is = ",s)