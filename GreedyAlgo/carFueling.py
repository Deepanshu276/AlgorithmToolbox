from array import *
arr=array("i",[1,2,5,7,10])
def fueling(d,n,arr1):
    numFueling=0
    startFueling=0
    while startFueling<d:
        endFuiling=startFueling
        while(startFueling<d and arr1[startFueling+1]-arr1[endFuiling]<=n):
            startFueling=startFueling+1
        if startFueling==endFuiling:
            return "IMPOSSIBLE"
        if startFueling<=d:
            numFueling=numFueling+1
    return numFueling
print(fueling(3,6,arr))

