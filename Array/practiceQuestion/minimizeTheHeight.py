# import numpy as np
# arr1=np.array([1, 9, 10 ,1, 1, 3, 10, 3 ,4 ,6])
# def height(arr,k):
#     max=0
#     min=0
#     curr=0
#     height=0
#     height1=0
#     for i in range(0,len(arr)):
#         if arr[i]-k<=0:
#             arr[i]+=k
#         else:
#             arr[i]-=k
    
#         curr=arr[i]
#         if curr>=max:
#             max=curr
#             min=i
#     print(arr)
#     print(max)
#     print(min)
#     # print(arr[min-1])
#     if min==len(arr)-1:
#         height=max-arr[min-1]
#     else:
#         height1=max-arr[min-1]
#         height=max-arr[min+1]
#     if height>height1:
#         return height
#     else:
#         return height1
#         # if min>curr:
#         #     min=curr
#         #height=max-min

#     #return height
# print(height(arr1,4))
    
import numpy as np
arr1=np.array([2 ,6, 3, 4, 7, 2, 10, 3, 2, 1])
def height(arr,k):
    np.sort(arr)
    minElement=0
    maxElement=0
    result=arr[-1]-arr[0]
    for i in range(len(arr)):
        
        if(arr[i]>=k):
            maxElement=max(arr[i-1]+k, arr[-1]-k)
            minElement=min(arr[0]+k,arr[i]-k)
    result=min(result,maxElement-minElement)
    return result

print(height(arr1,3))