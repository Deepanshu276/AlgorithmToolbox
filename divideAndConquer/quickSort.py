# def partition(customList, low, high):
#     i = low - 1
#     pivot = customList[high]
#     for j in range(low,high):
#         if customList[j] <= pivot:
#             i += 1
#             customList[i], customList[j] = customList[j], customList[i]
#     customList[i+1], customList[high] = customList[high], customList[i+1]
#     return (i+1)

# def quickSort(customList, low, high):
#     if low < high:
#         pi = partition(customList, low, high)
#         quickSort(customList, low, pi-1)
#         quickSort(customList, pi+1, high)
# z=int(input("")) 
# a=list(map(int,input("").split()))
# # quickSort(a,0,len(a)-1)
# for i in a:
#     print(i, end=" ")
# Uses python3
import sys
import random

def partition3(A, l, r):
    #write your code here
    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l   # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = A[l]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while i <= gt:      # Starting from the first element.
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
            
    return lt, gt

def randomized_quick_sort(A, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]

    lt, gt = partition3(A, l, r)
    randomized_quick_sort(a, l, lt - 1)
    randomized_quick_sort(a, gt + 1, r)
z=int(input("")) 
a=list(map(int,input("").split()))
randomized_quick_sort(a,0,len(a)-1)
for i in a:
    print(i, end=" ")
