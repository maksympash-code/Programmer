x = 0.9
print(1 / (1 + x))
s0 = 1
k = 0

while True:
    k += 1
    s0_new = s0
    s0 += ((-1) ** k) * (x ** k)
    if abs(s0 - s0_new) < 0.0000000001:
        break

print(s0)