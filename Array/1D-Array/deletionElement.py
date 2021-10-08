from array import *
arr1=array('i',[1,2,3,4,5])
arr1.insert(1,5)
def delete(m,n):
    for i in m:              # time complexity O(n^2)
        if i==n:             # space complexity O(1)
            arr1.remove(n)

delete(arr1,5)
print(arr1)