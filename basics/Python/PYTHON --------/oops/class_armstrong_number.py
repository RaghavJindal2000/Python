class Sample:
	def sum_digit(self,num): #12
		sum=0    
		while(num!=0):#12!=0     1!=0
			r=num%10  #r=12%10=2 r=1%10=1
			sum=sum+r*r*r#sum=8  sum=9
			num=num//10#num=12//10=1  num=0
		return sum
n=int(input("Enter the Number : "))#12
obj=Sample()
s=obj.sum_digit(n)
if(s==n):
	print("Armstrong Number")
else:
	print("Not Armstrong Number")
