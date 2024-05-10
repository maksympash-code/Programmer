from math import *

x = pi
print(sinh(x))

a0 = x
s0 = x
k = 1

while True:
    k += 2
    S0_new = s0
    s0 += (x ** k) / factorial(k)
    if abs(s0 - S0_new) < 0.000000001:
        break

print(s0)