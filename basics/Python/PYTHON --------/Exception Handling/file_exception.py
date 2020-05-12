try:
    f=open("C:/file/intro.txt","r")
    s=f.read()
    print(s)
    f.close()
except FileNotFoundError as f:
    print(f)