from math import *
def rec(x,k):
    res = (x ** (2*k + 1)) / factorial(2*k + 1)
    return res

x = float(input())
k = int(input())

if k >= 0:
    print(rec(x,k))
else:
    raise ValueError