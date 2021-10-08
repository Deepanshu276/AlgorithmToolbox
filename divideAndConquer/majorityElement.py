a=int(input(""))
y = list(map(int, input("").split()))
y.sort()
def majority(y,n):
    count=1
    for i in range(len(y)-1):
        if y[i]==y[i+1]:
            count=count+1
            if count>n/2:
                break
        else:
            count=1
            continue
    #print(count)
    if count>n/2:
        return 1
    else:
        return 0
print(majority(y,a))