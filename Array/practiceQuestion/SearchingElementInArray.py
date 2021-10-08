from array import *
arr1=array("i",[1,2,3,4,5,6,7,8,9])
def search(arr,n):
    for i in range(len(arr)):
        if arr1[i]==n:
            return arr1[i]
print(search(arr1,8))
