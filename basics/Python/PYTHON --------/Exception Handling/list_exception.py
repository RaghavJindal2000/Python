a=[10,20,30,"Hello",40,50,60]
for x in a:
	try:
		print(int(x))#a[6]	
	except:
		print("Index out of bound")
		break
	print("Thank you")