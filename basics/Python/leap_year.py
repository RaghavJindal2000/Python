year=int(input("Enter the Year Number :  "))
if(year%100==0):
    if(year%400==0):
        print(year," is Leap Year")
    else:
        print(year," is not a Leap Year")
else:
    if(year%4==0):
        print(year," is Leap Year")
    else:
        print(year," is not a Leap Year")
input()
