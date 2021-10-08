import numpy as np
arr1=np.array([23 ,41 ,84, -8, 42, -54, 1, 2, 28, 49, -32, -16 ,-33, -44, -100 ,-30, 68, -47, 59, -94, 35, -18])

def maxSum(arr):
    meh=0
    msf=float('-inf')
    for i in range(len(arr)):
        
        meh=meh+arr[i]
        if meh<arr[i]:
            meh=arr[i]
        if msf<meh:
            msf=meh
    return msf

print(maxSum(arr1))