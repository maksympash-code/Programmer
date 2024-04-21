from math import *
def rec(x,k):
    res = (-1) ** k * (x ** k) / factorial(k ** 2 + k)
    return res

x = float(input())
k = int(input())

if k >= 0:
    print(rec(x,k))
else:
    raise ValueError

