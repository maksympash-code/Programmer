from math import *
def gen(x,k):
    yield x,k
    res = (x ** (2*k)) / factorial(2 * k)
    yield res

x = int(input())
k = int(input())

iter_for_gen = iter(gen(x,k))

if k >= 0:
    print(next(iter_for_gen))
    print(next(iter_for_gen))
else:
    raise ValueError