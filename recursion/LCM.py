def gcd(a,b):
    if b==0:
        return a
    c=a%b
    return gcd(b,c)
def lcm(a,b):
    
    e=gcd(a,b)
    if b==0:
        return a
    c=a*b
    return int(c/e)
if __name__ == '__main__':
    input_n,input_m = map(int,input().split(" "))   
    #input_numbers = [int(x) for x in input().split()]
    print(lcm(input_n,input_m))
    
