a , b , n=[int(s) for s in input().split()]
a = a * n
b = b * n
if b >= 100:
    print(a + b//100, b % 100)
else:
    print(a,b)