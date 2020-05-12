a=int(input("Enter A : "))
b=int(input("Enter B : "))
try:
	c=a/b
	print("Ans : ",c)
except ZeroDivisionError as ze:
	print(ze)