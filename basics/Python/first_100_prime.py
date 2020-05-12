from math import sqrt
num=2
c=0
while(c<100):
    f=0
    for i in range(2,int(sqrt(num))+1):
        if(num%i==0):
            f=1
            break
    if(f==0):
        print(num,end="\t")
        c=c+1
    num=num+1
input()
