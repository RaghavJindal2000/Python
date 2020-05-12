# Bubble Sort
print("Enter Element in List\n")
a=[int(x) for x in input().split()]
print("Original List is \n",a)#[5,4,3,5,2]
for i in range(len(a)-1,0,-1):#(4,0,-1) i=4
	for j in range(0,i):#(0,4) j=0
		if(a[j]>a[j+1]):#(a[0]>a[1])5>4
				temp=a[j]#temp=5
				a[j]=a[j+1]#a[0]=4
				a[j+1]=temp#a[1]=5
print("Sorted List is \n",a)
