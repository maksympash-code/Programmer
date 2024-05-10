n = int(input("Введіть число члена,якого хочете обчислити:"))

a1 = 0
b1 = 1
a2 = 1
b2 = 1
S2 = 4

for k in range(3,n+1):
    bk = b2 + a2
    ak = a2 / k + a1 * bk
    S2 += (2 ** k) / (ak + bk)

print(S2)
