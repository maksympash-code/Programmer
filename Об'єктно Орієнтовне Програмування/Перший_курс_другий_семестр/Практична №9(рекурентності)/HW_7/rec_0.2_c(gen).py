from math import *
def gen(x,k):
    yield x,k
    res = (-1) ** k * (x ** k) / factorial(k ** 2 + k)
    yield res

x = float(input())
k = int(input())

iter_for_gen = iter(gen(x,k))

if k >= 0:
    print(next(iter_for_gen))
    print(next(iter_for_gen))
else:
    raise ValueError

