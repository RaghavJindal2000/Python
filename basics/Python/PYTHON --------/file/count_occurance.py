f=open("intro.txt","r")
str=f.read()
lv=0
lc=0
uv=0
uc=0
d=0
s=0
sp=0#str="Hello World"
for i in str:#i='e'
    if(ord(i)>=97 and ord(i)<=122):
        if(ord(i)==97 or ord(i)==101 or 
		ord(i)==105 or ord(i)==111 or ord(i)==117):
            lv=lv+1
        else:
            lc=lc+1
    elif(ord(i)>=65 and ord(i)<=90):
        if(ord(i)==65 or ord(i)==69 or 
		ord(i)==73 or ord(i)==79 or ord(i)==85):
            uv=uv+1
        else:
            uc=uc+1
    elif(ord(i)>=48 and ord(i)<=57):
        d=d+1
    elif(ord(i)==32):
        s=s+1
    else:
        sp=sp+1
print("Lower Case Vowels      = ",lv)
print("Lower Case Consonents  = ",lc)
print("Upper Case Vowels      = ",uv)
print("Upper Case Consonents  = ",uc)
print("Digits                 = ",d)
print("Space                  = ",s)
print("Special Character      = ",sp)
f.close()