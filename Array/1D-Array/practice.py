#create an array and traverse
from array import *
arr1=array('i',[1,2,3,4,6])
def traverse(n):
    for i in n:
        print(i)
traverse(arr1)

#Access individual element through indexes
print("question2")
print(arr1[0])

#append any value to the array using append method
print("question3")
arr1.append(10)
print(arr1)

#insert value in the array using insert() method
print("question 4")
arr1.insert(0,20)
print(arr1)

#extend python array using extend() method
print("question5")
arr1.extend([1,3,2])
print(arr1)

#add item from list into array usinh fromList() method
print("question 6")
arr1.fromlist([99,98,97])
print(arr1)

#remove any element using remove() method
print("question 7")
arr1.remove(1)
print(arr1)

#remove last array element using pop method
print("question 8")
arr1.pop()
print(arr1)

#fetch any element usinng its index using index() method
print("question 9")
def fetch(n):
    #for i in n:
    return arr1.index(n)
print(fetch(20))

#reverse array using reverse() method
print("question 10")
arr1.reverse()
print(arr1)

#get array buffer information using buffer_info() method
print("question 11")
print(arr1.buffer_info())
#check the number of occurences of an element using count() method
print("question 12")
def occurences(arr,n):
    return arr.count(n)
print(occurences(arr1,3))

#convert array to string using tostring() method
print("question 13")
# str=arr1.toString()
# print(str)
#convert array to python list using tolist() method
#print("question 14")
print(arr1.tolist())


#