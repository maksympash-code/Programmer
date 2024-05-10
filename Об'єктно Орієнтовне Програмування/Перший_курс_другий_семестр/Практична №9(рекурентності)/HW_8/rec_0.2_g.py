from math import *
x = 0.9
print(sqrt(1 + x))

s0 = 1
k = 0

while True:
    k += 1
    s0_new = s0
    s0 += (((-1)**k * factorial(2*k)) / ((1-2*k) * ((factorial(k)) ** 2) * 4 ** k)) * (x ** k)
    if abs(s0 - s0_new) < 0.0000000001:
        break

print(s0)