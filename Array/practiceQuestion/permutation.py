list=['l','i','e','p']
list1=['e','i','l','p','i']
list3=[]
def permuatation(list,list1):
    if len(list)!=len(list1):
        return False
    list1.sort()
    list.sort()
    if list==list1:
         return "they are permutation"
    return "they are not permutation"
    

print(permuatation(list,list1))