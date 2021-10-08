from array import *
import numpy as np
arr=array("i",[])
def jh(n):
    sum=0
    sum1=0
    for i in range(0,n+1):
        arr.append(i)
    if n==0:
        arr[0]=0
    if n>=1:
        arr[0]=0
        arr[1]=1
    for j in range(2,len(arr)):
        arr[j]=(arr[j-1]+arr[j-2])%10
        sum=arr[j]*arr[j]
        sum1=sum+sum1
    if n==0:
        print(sum1+arr[0])
    else:
        print((sum1 + arr[0] + arr[1])%10)

if __name__ == '__main__':
    input_n = int(input())
    #input_numbers = [int(x) for x in input().split()]
    jh(input_n)
