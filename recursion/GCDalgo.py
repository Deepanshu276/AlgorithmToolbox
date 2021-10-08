def gcd(a,b):
    if b==0:
        return a
    c=a%b
    return gcd(b,c)
if __name__ == '__main__':
    input_n,input_m = map(int,input().split(" "))   
    #input_numbers = [int(x) for x in input().split()]
    print(gcd(input_n,input_m))
    