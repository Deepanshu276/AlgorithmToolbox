from array import *

arr1=array('i',[1,2,3,4,5])

def accessingElement(n,index):
    if index >= len(n):            #time complexity is O(1)
        print("Please enter the index in range") # space complexity is O(1)
    else:
        print(n[index])

accessingElement(arr1,9)
