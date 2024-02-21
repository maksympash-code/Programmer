n = int(input())
lst1=[int(el1) for el1 in input().split()]

if n == len(lst1):
    lst1 = [lst1[n-1]] + lst1
    del lst1[n]
else:
    a = lst1[n-1]
    lst1[n-1] = lst1[n]
    lst1[n] = a

print(*lst1)
