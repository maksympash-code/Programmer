N=int(input())
lst=[int(el) for el in input().split()]

NEWlst=[]
for el in range (len(lst)):
    if lst[el] not in NEWlst:
        NEWlst.append(lst[el])

print(*NEWlst)
