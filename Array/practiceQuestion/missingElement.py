from array import *
arr1=array('i', [1,2,5,6,7,8,9,80,99])
def missing(array,n):
    for i in range(1,n+1):
        if i not in array:
            print("missing element is ", i)
missing(arr1,100)



