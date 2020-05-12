a=[10,20,30,40,50]
print("Original List is \n",a)
a[4]=100
print("Updated List is \n",a)
a.append(110)
print("Updated List after is \n",a)
a.insert(4,50)
print("Updated List after insertion is \n",a)
del a[5]
print("Updated List after Deletion is \n",a)
a.reverse()
print("Revered List is\n",a)
print("Sum of list Elements = ",sum(a))
a.sort()
print("Sorted List is\n",a)
a.sort(reverse=True)
print("Sorted List is\n",a)
input()
