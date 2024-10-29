from math import *

def F(x, y):
    return x**2 + atan(x*y) + y

def f(x, y):
    new = 1 / (x + 2)
    return y - new * F(x, y)

