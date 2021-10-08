def money(numbers):
    coins=[1,5,10]
    N=numbers
    coins.sort()
    index=len(coins)-1
    list=[]
    while True:
        coinsValue=coins[index]
        if coinsValue<=N:
            list.append(coinsValue)
            N=N-coinsValue
        if coinsValue>N:
            index=index-1
        if N==0:
            break
    return len(list)

if __name__ == '__main__':
    input_n = int(input())
    print(money(input_n))
