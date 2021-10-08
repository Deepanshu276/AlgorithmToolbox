import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
def search(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return "the postion is " + " " + str(i) + " " + str(j)
    return "the value is not found"

print(search(arr1,2)) 
