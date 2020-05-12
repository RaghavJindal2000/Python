def loginuser(f,a):
    print("Press 1 to Deposite\nPress 2 to Withdrawl\nPress 3 to exit")
    c = int(input("Enter Your Choice : "))
    if c==1:
        deposite(f,a)
    elif c==2:
        withdrawl()
    elif c==3:
        exit()
    else:
        print("Wrong Choice")

def deposite(f,a):
    amount = int(input("Enter Amount : "))
    am = int(a[-1])+amount
    f.write(f"{am}\n")
    print("Total Amount : ",am)
    f.close()
    old_customer()
def new_customer():
    name=input("Enter name : ")
    email=input("Enter email : ")
    phno=input("Enter phno. : ")
    username=input("Enter username : ")
    password=input("Enter password : ")
    amount=input("Enter amount : ")
    a=[name,email,phno,username,password,amount]
    f=open(f"{username}.txt","w")
    for x in a:
        f.write(f"{x}\n")
    f.close()
    print(" Account Created")
    main()

def old_customer():
    username=input("Enter username : ")
    password=input("Enter password : ")
    f=open(f"{username}.txt","r+")
    a = f.readlines()
    if a[4].strip()==password:
        print("Logged in")
        loginuser(f,a)
        f.close()
    else:
        print("try again")
        old_customer()
    main()

def main():
    print("Welcome to bank".center(50,"*"))
    print("press 1 for new customer\nPress 2 for old customer\nPress 3 for admin\Press 4 for exit")
    c=int(input("Enter your choice: "))
    if c==1:
          new_customer()
    elif c==2:
          old_customer()
    elif c==3:
          admin()
    elif c==4:
          exit()
    else:
          print("Invalid choice")
          main()
main()

          


          









        
