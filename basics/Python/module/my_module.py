def sort_selection(x):
    for i in range(0,len(x)-1):
        for j in range(i+1,len(x)):
            if(x[i]>x[j]):
                temp=x[i]
                x[i]=x[j]
                x[j]=temp
def sort_bubble(x):
    for i in range(len(x)-1,0,-1):
        for j in range(0,i):
            if(x[j]>x[j+1]):
                temp=x[j]
                x[j]=x[j+1]
                x[j+1]=temp
def reverse(x):
    for i in range(0,len(x)//2):
        temp=x[i]
        x[i]=x[len(x)-1-i]
        x[len(x)-1-i]=temp



        
