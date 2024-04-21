def rec(x , k):
    return (-1)**k * (x ** k) / k

x = float(input())
k = int(input())

if k >= 1:
    print(rec(x , k))
else:
    raise ValueError