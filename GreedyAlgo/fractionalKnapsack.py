class Item:
    def __init__(self,value,weight):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse = True)
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value
        
        if usedCapacity == capacity:
            break
    h="{0:.04f}".format(totalValue)
    print(h)
cList=[]
a,b=[int(x) for x in input().split()]
for i in range(a):
    c,d=[int(x) for x in input().split()]
    item1 =Item(c,d)
    cList.append(item1)

#     print(item1)
    #e,f=[int(x) for x in input().split()]
    #g,h=[int(x) for x in input().split()]
# a,b=[int(x) for x in input().split()]
# c,d=[int(x) for x in input().split()]
# e,f=[int(x) for x in input().split()]
# g,h=[int(x) for x in input().split()]
# item1 =Item(c,d)
# item2 = Item(e,f)
# item3 = Item(g,h)
# cList = [item1,item2,item3]
knapsackMethod(cList, b)