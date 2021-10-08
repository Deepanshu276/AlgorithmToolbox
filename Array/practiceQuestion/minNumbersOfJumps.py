import numpy as np
arr1=np.array([
    47, 76, 55 ,13, 2 ,48, 46, 27, 12, 37, 99, 25, 48, 83, 20, 77, 13, 9, 35, 55, 
    62, 76, 57, 18, 72, 64, 10,4, 64, 74, 63, 77, 15, 18, 91, 84, 32, 36, 77, 10, 
    39, 75, 35, 87, 23, 22, 30, 37, 31, 65, 58, 59, 7, 14,78 ,79, 45, 54, 83, 8, 
    94, 12, 86, 9, 97, 42, 93, 95, 44, 70, 5, 83, 10, 40,36, 34, 62, 66, 71, 59, 
    97, 95, 18, 3 ,8 ,62, 48, 19, 15, 98, 28, 8, 9])
def jumps(arr):
    count=0
    flag=0
    for i in range(0,len(arr)-1):
        if arr[i]==arr[i+1]==1:
            print(arr[i])
            count=count-1
    for j in range(0,len(arr)-1):
        flag=flag+arr[flag]
        count+=1
        
        if flag>=len(arr)-1:
            break
    if flag>=len(arr)-1:
        return count
    else:
        return -1
       
print(jumps(arr1))
