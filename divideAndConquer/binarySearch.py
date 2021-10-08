import math
#from array import *
z=int(input(""))
x = list(map(int, input("").split()))
a=int(input(""))
y = list(map(int, input("").split()))
def search(x,start,end,n):
        mid=math.floor((start+end)/2)
        if end<start:
            print(-1,end=" ")
            return end-1
        
        if n==x[mid]:
            print(mid,end=" ")
        elif n<=x[mid]:
            return search(x,start,mid-1,n)
        else:
            return search(x,mid+1,end,n)
for i in y:

    search(x,0,len(x)-1,i)

    
