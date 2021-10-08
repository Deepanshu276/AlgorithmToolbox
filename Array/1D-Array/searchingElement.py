from array import *
arr1=array('i',[1,2,3,4,6,7,8,5])
def searchingElement(n,i):
    for j in n:
        if j==i:
            print("element found at ", j , "position" )
          
    return "element not found! Try some other element"
            # time complexity O(n)
            #space complexity O(1)
           
     

searchingElement(arr1,12)