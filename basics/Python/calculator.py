print("Enter the Two Numbers : ")
a=int(input())
b=int(input())
print("Press + for Additon")
print("Press - for Subtraction")
print("Press * for Multiplication")
print("Press / for Division")
print("Press // for Floor Division")
print("Press % to Get Remainder")
print("Enter Your Choice :  ")
ch=input()
if(ch=="+"):
    print("%d + %d = %d"%(a,b,a+b))
    #print(a,"+ ",b," = ",a+b)
elif(ch=="-"):
    print("%d - %d = %d"%(a,b,a-b))
    #print(a,"- ",b," = ",a-b)
elif(ch=="*"):
    print("%d * %d = %d"%(a,b,a*b))
    #print(a,"* ",b," = ",a*b)
elif(ch=="/"):
    print("%d / %d = %d"%(a,b,a/b))
    #print(a,"/ ",b," = ",a/b)
elif(ch=="//"):
    print("%d // %d = %d"%(a,b,a//b))
    #print(a," // ",b," = ",a//b)
elif(ch=="%"):
    print(a,"% ",b," = ",a%b)
input()
