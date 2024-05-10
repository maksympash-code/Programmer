from math import *
n = int(input("Введіть число члена,якого хочете обчислити:"))

a1 = 1
a2 = 1
S2 = 3

for k in range(3,n+1):
    ak = a2 + a1 / (2 ** k)
    S2 += factorial(k) / ak

print(S2)