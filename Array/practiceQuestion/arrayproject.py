list=[]
while(True):
    inp=int(input("How many day's tempreture : "))
    inp1=inp
    if inp1==0:
        print("Plaese enter the correct number of day :")
        break
    for i in range(inp1):
        inp2=int(input("Day High temperature : "))
        inp3=inp2
        list.append(inp3)
    break
avg=sum(list)/len(list)
print("Average : " ,avg)
count=0
for j in range(len(list)):
    if list[j]>avg:
        count+=1
print(count, "day(s) above average")
    

