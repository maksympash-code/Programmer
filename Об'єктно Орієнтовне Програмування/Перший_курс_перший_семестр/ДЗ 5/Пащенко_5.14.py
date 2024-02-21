n, k= [int(d) for d in input().split()]
a=[int(el) for el in input().split()]

a.sort()

for el in a:
    l=a[k-1]

print(l)