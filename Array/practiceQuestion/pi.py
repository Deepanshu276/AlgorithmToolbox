# def Factorial(N):
#     fact=1
    
#     for i in range(N):
#         fact=(N-i)*fact
        
#     for i in range(1,N+1):
#         if i==N:
#             print(i,'=',fact)
#         else:
#             print(i,'* ',end='')
# Factorial(10)
import numpy as np
#arr1=np.array([9,2,6,4,1])
def product1(A):
    min=0
    max=0
    A.sort()
    min=A[0]
    max=A[-1]
    product2=min*max
        
    return product2
print(product1(A))
