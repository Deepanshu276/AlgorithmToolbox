from array import *
arr1=array("i",[1,12,3,4,5,6,7,10])
max1=0
max2=0
arr2=array("i",[])
def product(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            max1=arr[i]*arr[j]
            arr2.append(max1)
    print(max(arr2))

        

product(arr1)

