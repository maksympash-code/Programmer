x = 0.9
print(1 / ((1 + x)**2))

s0 = 1
k = 0

while True:
    k += 1
    s0_new = s0
    s0 += ((-1) ** k) * (k+1) * (x**k)
    if abs(s0 - s0_new) < 0.00000000001:
        break

print(s0)