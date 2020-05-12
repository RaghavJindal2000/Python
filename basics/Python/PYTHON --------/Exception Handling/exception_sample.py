while True:
	try:
		a=int(input("Enter the First Number : "))
		b=int(input("Enter the Second Number : "))
		print(a/b)
		print("Division is Complete")
	except ZeroDivisionError as z:
		print(z)	
	except ValueError as vt:
		print(vt)
		break
	finally:
		print("Thank You")	