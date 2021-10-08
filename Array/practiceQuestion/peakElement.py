# import numpy as np
# arr1=np.array([213 ,509, 129, 898, 766, 198, 131
# ])
# def peak(arr):
#     max=0
#     curr=0
#     for i in range(0,len(arr)-1):
         
#             if arr[i]<arr[i+1]:
#                 curr=i+1
#             if curr>max:
#                 max=curr
                  
#     return max 



# print(peak(arr1))
import numpy as np
arr1=np.array([1,2,3,3,2])
arr1.sort()
v=int(len(arr1)/2)
print(arr1[v])

print(arr1)
           





