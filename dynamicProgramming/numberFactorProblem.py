#top down
def number(n,dp):
    if n==1 or n==0 or n==2:
        return 1
    elif n==3:
        return 1
    if n in dp:
        return dp[n]
    else:
        rec1=number(n-1,dp)
        rec2=number(n//2,dp)
        rec3=number(n//3,dp)
        #dp[n]=rec1+rec2+rec3
        return dp[n]
dic={}
print(number(5,dic))
#down top
def number(n,dp):
    if n in dp:
        return dp[n]
    for i in range(4,n+1):
        dp.append(dp[i-1]+dp[i-3]+dp[i-4])
    return dp[n]
dp=[1,1,1,2]
print(number(5,dp))
