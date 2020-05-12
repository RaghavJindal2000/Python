file1 = open(input("Please wish to open:" ),"r")## Open the file and "r" read it
emp = 0
y = 0
for x in file1:
	x = x[0:1]
	print(x)	## Take the whole 1st value.
	x = float(x)## Convert from string to number
	x = x + emp ## Add it to the zero
	y = y + 1.0 ## Add one to the y to account for each value inputed.
	emp = x ## This will add the old value to the new value
	float(y)
	print ("Here is the average of the numbers inputed",x / y)
