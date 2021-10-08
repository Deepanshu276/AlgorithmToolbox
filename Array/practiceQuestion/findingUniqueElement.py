list=[1,3,4,2,5,6,7,8]
def unique(list1):
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]==list1[j]:
                return False
    return True       
print(unique(list))


