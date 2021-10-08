# import numpy as np
# def factorial(N):
#     list=[]
#     list1=[]
#     fact=1
#     s='*'
#     for i in range(N):
#         fact=(N-i)
#         fact1=str(fact)
#         list.append(fact1)
#         list.reverse()
#     print("*".join(list))
#     list1=int(list)
#     str1=np.product(list1)
#     print(str1)
#     #for i in list:
    


#     # for i in range(1,len(list)):
#     #         print (str(list[-1]) + '*' + str(list[-i-1]) + str('=') + str(str1))
#         # for j in list:
#         #     print()

#     return fact
# print(factorial(5))

from array import *
arr=array("i",[])
def jh(n):
    for i in range(n):
        arr.append(i)
    print(arr)
jh(6)