import numpy as np
arr1=np.array([1, 2, 3, 4, 5])
def rot(arr):
    for i in range(0,len(arr)-1):
        temp=arr[i]
        arr[i]=arr[-1] 
        arr[-1]=temp
    return arr
print(rot(arr1))