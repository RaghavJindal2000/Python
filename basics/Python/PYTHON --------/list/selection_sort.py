#sorting alogirthms
#Selection sort
#Bubble Sort
#Insertion Sort
#Quick Sort
#Merge Sort
#Heap Sort
# Selection Sort
print("Enter Element in List\n")
a=[int(x) for x in input().split()]
print("Original List is \n",a)#[6 5 4 8 5]
for i in range(0,len(a)-1):#(0,4) i=0,
	for j in range(i+1,len(a)):#(1,5) j=1,2
		if(a[i]>a[j]):#(a[0]>a[2])(5>4)
				temp=a[i]#temp=6
				a[i]=a[j]#a[0]=a[4] a[0]=5
				a[j]=temp#a[4]=6
print("Sorted List is \n",a)
