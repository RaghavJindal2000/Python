import csv
c= [['Person', '\tAge'], 
		['Peter', '22'], 
			['Jasmine', '21'], 
			['Sam', '24']]
with open('person.csv', 'w') as s:
	w = csv.writer(s,lineterminator="\n")
	w.writerows(c)
