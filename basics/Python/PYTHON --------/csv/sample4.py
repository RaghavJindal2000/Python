import csv
with open('people1.csv') as c:
	w= csv.reader(c)
	e=list(w)
	for x in e:
		for i in x:
			if i.isdigit():
				print(i)