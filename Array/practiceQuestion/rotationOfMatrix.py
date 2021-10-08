import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
def rotation(arr1):
    n=len(arr1)
    for layer in range(n//2):
        first=layer
        last=n-layer-1
    for i in range(first,last):
        #save top element
        top=arr1[layer][i]
        #move bottom element to top
        arr1[layer][i]=arr1[-1-i][layer]
        #move right element to left
        arr1[-1-i][layer]=arr1[layer-1][-1-i]
        # move top element to bootom
        arr1[layer-1][-1-i]=arr1[i][layer-1]
        #move topleft element to top right
        arr1[i][layer-1]=top
    return arr1

print(rotation(arr1))


        