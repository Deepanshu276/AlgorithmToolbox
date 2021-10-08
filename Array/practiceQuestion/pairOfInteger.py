list=[1,2,3,5,0,4,1,2,1,2,3]
for i in range(len(list)):
    if list[i-1]==list[i]:
        continue
    elif list[i-1]+list[i]==5:
        print(i-1,i)