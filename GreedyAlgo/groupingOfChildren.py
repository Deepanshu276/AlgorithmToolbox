from array import *
arr=array("i",[1,2,65,4,6,8,9,11])
def group(arr1,n):
    i=0
    R=set()
    while(i<n):
        l,r=arr1[i],arr1[i+1]
        R=R.union({(l,r)})
        i=i+1
        while i<n and arr1[i]<=r:
            i=i+1
    return R
print(group(arr,len(arr)))
