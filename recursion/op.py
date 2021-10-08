# from array import *
# arr=array("i",[])
# def jh(n,m):
#     sum=0
#     for i in range(0,n+1):
#         arr.append(i)
#     if n==0:
#         arr[0]=0
#     if n>=1:
#         arr[0]=0
#         arr[1]=1
#     for j in range(2,len(arr)):
#         arr[j]=(arr[j-1]+arr[j-2])
#         arr[j]=arr[j]%m
#     return (arr[j])

# if __name__ == '__main__':
#     input_n,input_m = map(int,input().split(" "))   
#     #input_numbers = [int(x) for x in input().split()]
#     print(jh(input_n,input_m))

num = 3316
list1=[]
for a in str(num):
    x=int(a)
    list1.append(x)
if (list1[0]+list1[1])==(list1[-2]+list1[-1]):
    print("yes")
