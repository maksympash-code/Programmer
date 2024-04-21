from math import *

def gen(x,k):
    yield x,k
    x = (x ** (2*k + 1)) / factorial(2*k + 1)
    yield x

x = float(input())
k = int(input())

iter_for_gen = iter(gen(x,k))

if k >= 0:
    print(next(iter_for_gen))
    print(next(iter_for_gen))
else:
    raise ValueError