num=int(input("Enter the Number :  "))#123
sum=0
while(num!=0):
	r=num%10#2
	sum=sum+r#5
	num=num//10#1
print("Sum of Digits = ",sum)
