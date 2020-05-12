print("Enter Element in List")
a=[int(x) for x in input().split()]
print("Original List is \n",a)
a.sort()#[1,2,3,4,5]
start=0
end=len(a)-1#end=4
mid=int((start+end)/2)#2
n=int(input("Enter the Number to Search in list "))#4
while(n!=a[mid] and start<=end):#(4!=4 and 0<=4)
	if(n<a[mid]):#(4<3)
		end=mid-1
	else:
		start=mid+1#start=3
	mid=int((start+end)/2)#mid=3
if(n==a[mid]):
	print(n,"  Exist in List at a[",mid,"]")
else:
	print(n,"Does not Exist in List")


#Time Complexity of Linear Search = O(n)
#Time COmplexity of Binary Search O(log2n): log(n)/log(2)