from math import *
x = 0.5
print(log((1+x) / (1-x)))

s0 = x
k = 1

while True:
    k += 2
    s0_new = s0
    s0 += x ** k / k

    if abs(s0 - s0_new) < 0.000000000001:
        break

print(s0 * 2)