num=int(input("Enter the Number : "))
sum=0
temp=num
while(temp!=0):     #1729   172     17      1
    r=temp%10       #9      2       7       1
    sum=sum+r       #0+9=9  9+2=11  11+7=18 18+1=19
    temp=temp//10   #172    17      1       0
temp=sum
rev=0
while(temp!=0):     #19         1
    r=temp%10       #9          1
    rev=rev*10+r    #0*10+9=9   9*10+1=91
    temp=temp//10   #1          0
if(sum*rev==num):
    print("Magical Number")
else:
    print("Not a Magical Number")
input()





