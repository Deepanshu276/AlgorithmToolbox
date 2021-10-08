import numpy as np
arr1=np.array([421, 548, 421, 548, 421])
def occur(arr1,k):
    count=0
    list=[]
    z=0
    j=int(len(arr1)/k)
    print(j)
    for i in range(len(arr1)):
        if arr1[i]>=j:
            list.append(arr1[i])
            list.sort()
    print(list)
    for h in range(0,len(list)-1):
        if list[h]==list[h+1]:
            count=count+1
        if j==count:
            z=z+1
            count=0
        if list[h]!=list[h+1]:
            count=0
        if list.count(list[0])==len(list):
            return 1
       

               
    return z
        
        



print(occur(arr1,3))