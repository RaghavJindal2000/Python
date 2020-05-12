import sys
sys.path
['','C:/Users/Dell/Desktop/Django/']
from samp import *
a=[]
b=int(input("Enter Range : "))
for x in range(b):
	c=int(input("Enter Element : "))
	a.append(c)
print(a)
ch=int(input("Press 1 for sorting : \n Press 2 for reverse :\n"))
if(ch==1):
	v=samp.sort_list(a)
	print(v)
elif(ch==2):
	v=samp.reverse_list(a)
	print(v)
else:
	print("Invalid Choice")	