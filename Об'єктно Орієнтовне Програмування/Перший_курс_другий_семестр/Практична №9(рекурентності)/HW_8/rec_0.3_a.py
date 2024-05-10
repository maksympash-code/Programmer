from math import *

x = int(input("Введіть x:"))
e = float(input("Введіть epsilon:"))
s0 = 1
k = 0
ak = 1
if e > 0:
    while True:
        k += 1
        ak *= x**2 / (2 * k)
        s0_new = s0
        s0 += ak
        if abs(s0 - s0_new) < e:
            break
    print(s0, k)
else:
    raise ValueError


