import csv
with open('person1.csv', 'r') as f:
	r = csv.reader(f)
	print(r)
	l = list(r)
	print(l)	
with open('sample1.csv', 'w') as writeFile:
    writer = csv.writer(writeFile,lineterminator="\n")
    writer.writerows(l)
