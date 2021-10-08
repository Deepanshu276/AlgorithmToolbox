from array import *

arr1=array('i',[1,2,3,5,8])
arr2=array('d',[1.2,2.1])

arr1.insert(0,10)
print("Inserting at start = ", arr1)#time complexity O(1)
arr1.insert(6,15)
print(" Inserting at Last = ", arr1)# time complexity O(n)
arr1.insert(4,20)
print("Inserting in between= ", arr1)# time complexity O(n)
