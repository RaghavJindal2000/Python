f=open('abcd.txt')
f.write(name)
print("File created")
f.close()
f=open('abcd.txt')
a=f.read()
print(a)