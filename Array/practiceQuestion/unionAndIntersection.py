import numpy as np
arr1=np.array([1, 1, 2, 2 ,3 ,3])
arr2=np.array([8, 9, 7, 6, 5])
def union(arr1,arr2):
    arr3=len(set(arr1)|set(arr2))
    return arr3
    
print(union(arr1,arr2))