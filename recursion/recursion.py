from array import *
arr=array("i",[])
def jh(m,n):
    for i in range(0,n+1):
        arr.append(i)
    if n==0:
        arr[0]=0
    if n>=1:
        arr[0]=0
        arr[1]=1
    for j in range(2,len(arr)):
        arr[j]=(arr[j-1]+arr[j-2])
    return arr[n]
if __name__ == '__main__':
    input_n = int(input())
    #input_numbers = [int(x) for x in input().split()]
    print(jh(input_n))
