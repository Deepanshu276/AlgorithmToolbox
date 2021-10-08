import numpy as np
from numpy.core.records import array
arr1=np.array([100,20,39,51,32,60,98,9,8])

arr1.sort()
def find(arr1,k):
    return arr1[k-1]

print(find(arr1,3))
