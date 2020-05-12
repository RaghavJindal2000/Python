def fact(num):#num=4
	if(num<=0):
		return 1
	else:
		print('num : ',num)#5 
		return num*fact(num-1) 			
n=int(input('Enter the number to get Factorial '))#5
f=fact(n)#f=fact(5)
print("Factorial",f)0