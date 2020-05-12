"""
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
"""
s="A"
for i in range(1,6):
    for j in range(1,6):
            print(s,end="")
    s=chr(ord(s)+1)
    print()
input()
