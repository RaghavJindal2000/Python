id=input("Enter the Employee Id :  ")
name=input("Enter the Name   :   ")
dsg=input("Enter the Designation : ")
basic=int(input("Enter the Basic Salary :  "))
l=int(input("Enter the Total Leaves :  "))

ta=basic*5//100
da=basic*6//100
hra=basic*7//100
lamount=basic/30*l
itax=basic*5/100
ma=3500

gross=basic+ta+da+hra+ma
net=gross-itax-lamount

print("------>>>>> Salary Slip <<<<<---------")
print("Emplpoyee Id     :        ",id)
print("Basic Salay      :        ",basic)
print("Name             :        ",name)
print("Designation      :        ",dsg)
print("--------------------------------------")
print("Total Leaves     :        ",l)
print("Leave Amount     :        ",lamount)
print("--------------------------------------")
print("Ta\tDa\tHra\tMa")
print(ta,"\t",da,"\t",hra,"\t",ma)
#print("%d\t%d\t%d\t%d"%(ta,da,hra,ma))
print("--------------------------------------")
print("Gross Salary    :          ",gross)
print("Income Tax      :          ",itax)
print("Net Salary      :          ",net)
print("--------------------------------------")
input()















