import numpy as np
arr1=np.array([-8 ,9 ,5 ,10, 2 ,6, -7, 7])
def move(arr):
    for i in range(0,len(arr)):
        if arr[i]<0:
            if(arr[i]<arr[i+1]):
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    return arr
print(move(arr1))

