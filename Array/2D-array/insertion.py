import numpy as np
arr1=np.array([[1,2,3,4],[5,6,7,8],[2,4,6,8]])
#arr2=np.insert(arr1,0,[[10,9,8]],axis=1) #time complexity O(mn)
arr2=np.append(arr1,[[0,9,7,1]], axis=1)
print(arr2)