"""
11111
*****
33333
*****
55555
"""
for i in range(1,6):
    for j in range(1,6):
        if(i%2==0):
            print("*",end="")
        else:
            print(i,end="")
    print()
input()
