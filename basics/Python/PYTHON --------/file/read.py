f=open("intro.txt")
b=f.read()
print(b)
f.seek(6)
print(f.tell())
a=f.readline()
print(a)
f.seek(0)
str2=f.readlines()
print(str2)
