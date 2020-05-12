ch=input("Enter the Character :  ")
if(ord(ch)>=ord("a") and ord(ch)<=ord("z")):
    if(ord(ch)==ord("a") or ord(ch)==ord("e") or ord(ch)==ord("i") or ord(ch)==ord("o") or ord(ch)==ord("u")):
        print("Lower Case Vowel")
    else:
        print("Lower Case Consonent")
elif(ord(ch)>=ord("A") and ord(ch)<=ord("Z")):
    if(ord(ch)==ord("A") or ord(ch)==ord("E") or ord(ch)==ord("I") or ord(ch)==ord("O") or ord(ch)==ord("U")):
        print("Upper Case Vowel")
    else:
        print("Upper Case Consonent")
elif(ord(ch)>=ord("0") and ord(ch)<=ord("9")):
    print("Digit")
elif(ord(ch)==ord(" ")):
    print("Space")
else:
    print("Special Character")
input()
    
