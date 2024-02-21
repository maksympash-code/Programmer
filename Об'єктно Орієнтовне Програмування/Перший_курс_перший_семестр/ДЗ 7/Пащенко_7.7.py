def nsd(a, b):
    if a < b:
        a,b = b,a
    while b > 0:
        a, b = b, a % b

    return a

def nsk(a):
    for i in range(2, a+1):
        if a % i == 0:
            continue
        else:
            a *= int(i / nsd(a,i))
    return a




a = int(input())
print(nsk(a))
# print(nsk(A))