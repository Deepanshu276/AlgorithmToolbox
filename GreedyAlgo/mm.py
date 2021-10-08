def numbers(n):
    max1=0
    flag=2
    for i in range(1,n):
        
        if(max1+i+flag==n):
            print(max1,i,flag)
            max1=max1+1
            flag=flag+1
            i=0
numbers(6)
