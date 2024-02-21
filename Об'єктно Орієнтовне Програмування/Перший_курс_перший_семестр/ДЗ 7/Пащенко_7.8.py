def nsd(a, b):
    if a < b:
        a,b = b,a
    while b > 0:
        a, b = b, a % b

    return a

def nsk(a , b):
    nsk = a * b // nsd(a,b)
    return nsk

a , b = [int(d) for d in input().split()]

counter = 0

for i in range(a, b + 1 , a):
    c = a * b // i
    if nsd(i,c) == a and nsk(i,c) == b:
        counter += 1

print(counter)