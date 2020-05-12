import csv
person = [['SN', 'Person', 'DOB'],
['1', 'John', '18/1/1997'],
['2', 'Marie','19/2/1998'],
['3', 'Simon','20/3/1999'],
['4', 'Erik', '21/4/2000'],
['5', 'Ana', '2/12/2001']]

with open('person1.csv', 'w') as f:
	w = csv.writer(f,lineterminator="\n")
	w.writerows(person)