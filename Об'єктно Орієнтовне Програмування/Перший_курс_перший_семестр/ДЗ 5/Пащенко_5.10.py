n=int(input())
lst1=[int(el1) for el1 in input().split()]
m=int(input())
lst2=[int(el2) for el2 in input().split()]

lst3=[]

for el1 in lst1:
    if el1 not in lst2:
        lst3.append(el1)


print(len(lst3))
print(*lst3)