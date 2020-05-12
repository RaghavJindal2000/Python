import sys
a = ['a', 0, 2]
for entry in a:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        print(r)
    except:
        print("Oops!",sys.exc_info()[1],"occured.")
