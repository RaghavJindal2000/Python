def pattern(i,j):
    if(i>5):
        return
    elif(j<=5):
        print("*",end="")
        pattern(i,j+1)
    else:
        print()
        pattern(i+1,1)
pattern(1,1)
input()
