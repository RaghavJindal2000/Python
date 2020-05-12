from os import chdir,getcwd
chdir("F:/Python/py")
f=open('hello.txt','w')
f.write("Hello world")
f.close()
print(getcwd())