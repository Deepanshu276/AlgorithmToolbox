a=input()
input_numbers = [int(x) for x in input().split()]
input_numbers.sort()
input_numbers1 = [int(x) for x in input().split()]
input_numbers1.sort()
max=0
for i in range(len(input_numbers)):
    z=input_numbers[-i-1]*input_numbers1[-i-1]
    max=z + max 
print(max)
