from itertools import permutations
def largest(l):
    lst = []
    for i in permutations(l, len(l)):
#         # provides all permutations of the list values,
#         # store them in list to find max
        lst.append("".join(map(str,i)))
    return max(lst)
 
print(largest([5,52,57,517,532,569,581]))
# list=[5,7,3,9,1,9]
# list1=[]
# list.sort(reverse=True)
# list1=list[:]
# print(list1)
# list1=[]
# max1=0
# max2=0
# index=0
# for i in range(0,len(list)):
#     for j in range(i,len(list)):
#         if list[i]<list[j]:
#             max1=list[j]
#             if max2<max1:
#                 max2=max1
#                 index=j
#         if len(list)==0:
#             break
# list1.append(max2)
# list.pop(index)
# print(list1)
# print(list)
