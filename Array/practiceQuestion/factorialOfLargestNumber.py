import numpy as np
arr1=np.array([1,2,6])
def factorial(arr):
    max=0
    curr=0
    fact=1
    for i in range(0,len(arr)-1):
        if arr[i]<arr[i+1]:
            curr=arr[i+1]
        if max<curr:
            max=curr
    for i in range(max):
        fact=(max-i)*fact
    return fact
    

print(factorial(arr1))

