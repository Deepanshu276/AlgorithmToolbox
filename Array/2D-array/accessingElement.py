import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
def access(arr,row,col):
    if row>=len(arr) and col>=(arr[0]):
        print("Please enter the correct index")
    else:
        print(arr[row][col])
access(arr1,2,1) 