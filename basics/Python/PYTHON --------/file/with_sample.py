count = 0
with open("intro.txt") as f:
	for x in f:
		print(x)
		count+=1
	print(f.closed)	
print("NO. of lines",count)
print(f.closed)