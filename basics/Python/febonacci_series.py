#febonaci Series: 0 1 1 2 3 5 8 13 21 34 55 89..
num=int(input("Enter the Last Term Range of Febonacci Series:  "))
a=0
b=1
sum=a+b
print(a,"\t",b,end="\t")
while(sum<=num):
    print(sum,end="\t")
    a=b
    b=sum
    sum=a+b
input()
#num=50
#a=0   1 1 2 3 5  8  13 21
#b=1   1 2 3 5 8  13 21 34
#sum=1 2 3 5 8 13 21 34 55
#o/p 0 1 1 2 3 5 8 13 21 34
