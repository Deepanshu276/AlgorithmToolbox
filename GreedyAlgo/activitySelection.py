list=[["A1",0,6],
      ["A2",3,4],
      ["A3",1,2],
      ["A4",5,8],
      ["A5",5,7],
      ["A6",8,9]]

def activity(list1):
    list1.sort(key=lambda x:x[2])
    i=0
    firstA=list1[i][0]
    print(firstA)
    for j in range(1,len(list1)):
        if list1[j][1]>list1[i][2]:
            
            print(list1[j][0])
            i=j
activity(list)