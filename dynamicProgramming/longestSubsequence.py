t={}
def seq(a,i):
    if i not in t:
        t[i]=1
    for j in range(i):
        if a[j]<a[i]:
            t[i]=max(t[i],seq(a,j)+1)
    return t[i]
a = [ 7 , 2 , 1 , 3 , 8 , 4 , 9 , 1 , 2 , 6 , 5 , 9 , 3]
print(max(seq(a, i ) for i in range (len(a))))
