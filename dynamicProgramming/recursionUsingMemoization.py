# def recursion(n,memo):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     if n not in memo:
#         memo[n]=recursion(n-1,memo)+recursion(n-2,memo)
#     return memo[n]
# dic={}
# print(recursion(6,dic))

"""fibonacci using bottom up tabulation"""
def fib(n):
    tab=[0,1]
    for i in range(2,n+1):
        tab.append(tab[i-1]+tab[i-2])
    return tab[n-1]

print(fib(6))
