import csv
with open('employee_file2.csv','w') as csv_file:
	names = ['emp_name', 'dept', 'birth_month']
	w = csv.DictWriter(csv_file, fieldnames=names,lineterminator='\n')
	w.writeheader()
	w.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 
	'birth_month': 'November'})
	w.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 
	'birth_month': 'March'})
	w.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT'})
	