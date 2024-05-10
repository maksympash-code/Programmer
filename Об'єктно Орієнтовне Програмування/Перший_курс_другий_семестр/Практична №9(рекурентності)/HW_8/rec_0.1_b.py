n = int(input("Введіть число члена,якого хочете обчислити:"))

a1 = 1
a2 = 1
S2 = 12

for k in range(3,n+1):
    ak = a2 / k + a1
    S2 += (3 ** k) / ak

print(S2)