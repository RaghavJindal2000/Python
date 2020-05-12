from pymysql import *
def add_details():
    con=connect(db="Ducat",user="root",password="root",host="localhost")
    cur=con.cursor()
    id=int(input("Enter the Id of Employee : "))
    name=input("Enter the Name          :  ")
    basic=int(input("Enter the Basic Salary :  "))
    dn=int(input("Enter the Departement Number :  "))
    age=int(input("Enter the Age of Employee   :  "))
    cur.execute("insert into employee values(%d,'%s',%d,%d,%d)"%(id,name,basic,dn,age))
    con.commit()
    print("Record Inserted")
    con.close()
def display():
    con=connect(db="Ducat",user="root",password="root",host="localhost")
    cur=con.cursor()
    cur.execute("Select * from employee")
    result=cur.fetchall()
    con.commit()
    print("Id\tName\tSalary\tDno\tAge")
    for x in result:
        print("%d\t%s\t%d\t%d\t%d"%(x[0],x[1],x[2],x[3],x[4]))
    con.close()
def edit():
    con=connect(db="Ducat",user="root",password="root",host="localhost")
    cur=con.cursor()
    num=int(input("Enter the Id to Edit "))
    sal=int(input("Enter the Basic Salary to Update "))
    cur.execute("update employee set saalry = %d where id = %d"%(sal,num))
    con.commit()
    print("Record Updated")
    con.close()
def search():
    con=connect(db="Ducat",user="root",password="root",host="localhost")
    cur=con.cursor()
    num=int(input("Enter the Id to Search "))
    cur.execute("Select * from employee where id = %d"%num)
    x=cur.fetchone()
    con.commit()
    print("Id\tName\tSalary\tDno\tAge")
    print("%d\t%s\t%d\t%d\t%d"%(x[0],x[1],x[2],x[3],x[4]))
    con.close()
def delete():
    con=connect(db="Ducat",user="root",password="root",host="localhost")
    cur=con.cursor()
    num=int(input("Enter the Id to Delete "))
    cur.execute("delete from employee where id = %d"%(num))
    con.commit()
    print("Record Deleted")
    con.close()
while True:
    input("Press any key to Continue")
    print("\n\n\nPress 1 to add Record of Employee in to Table")
    print("Press 2 to Display All Record of Employee")
    print("Press 3 to Edit Record of Employee in to Table")
    print("Press 4 to Search Record of Employee from Table")
    print("Press 5 to Delete Record of Employee from Table")
    print("Press 6 to Exit")
    ch=int(input("Enter Your Choice "))
    if(ch==1):
        add_details()
    elif(ch==2):
        display()
    elif(ch==3):
        edit()
    elif(ch==4):
        search()
    elif(ch==5):
        delete()
    elif(ch==6):
        exit()
    else:
        print("Invalid Choice")
