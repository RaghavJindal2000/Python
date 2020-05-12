with open("sample1.csv","w") as f:
	for x in range(10):
		f.write("Hello\n")
	print(f.closed)	
print(f.closed)		
			