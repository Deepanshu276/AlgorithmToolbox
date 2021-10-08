import numpy as np
arr1=np.array([1,2,3,4,3])
print(arr1.sort())
def duplicate(arr1):
    arr2=np.array([])
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            arr2=np.insert(arr2,i,arr1[i])
        else:
            return arr1[i]
print(duplicate(arr1))
