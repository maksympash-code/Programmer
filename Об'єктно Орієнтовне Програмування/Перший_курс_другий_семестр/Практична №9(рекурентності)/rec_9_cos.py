from math import *

x = pi/6
print(cos(x))


s0 = x
a0 = x
n = 0

while abs(a0) >= 0.00001:
    n += 1
    a0 = (x**2) / (2 * n * (2*n - 1)) * a0
    s0 = s0 + a0

print(s0,n)

