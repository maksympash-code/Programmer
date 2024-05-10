from math import *
x = 0.9
print(log(x+1))
k = 1
s0 = x

while True:
    k += 1
    s0_new = s0
    s0 += ((-1) ** (k-1)) * ((x**k) / k)
    if abs(s0 - s0_new) < 0.000000001:
        break

print(s0)