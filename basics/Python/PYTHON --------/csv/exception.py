a=int(input("Enter First Number:  "))
try:	
	if(a<5):
		raise ZeroDivisionError
	else:
		raise ValueError
except ZeroDivisionError as ab:
	print("World")
except ValueError as v:
	print("Hello")