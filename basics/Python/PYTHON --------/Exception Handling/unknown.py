try:
	f = open("intro.txt")
	a=f.read()
	print(a)
	print(f.closed)
except:
	print("File not found")
finally:
   f.close()
   print(f.closed)
