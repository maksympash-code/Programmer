
x = float(input("Введіть будь яке число:"))
e = float(input("Введіть epsilon > 0"))
s0 = x
ak = x
k = 0
while True:
    k += 1
    s0_new = s0
    ak *= - ((x**2) * (2*k-1)) / (k * (2*k+1))
    s0 += ak
    if abs(s0 - s0_new) < e:
        break

print(s0, k)