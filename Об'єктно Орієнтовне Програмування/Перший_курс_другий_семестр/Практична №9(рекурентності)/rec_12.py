x = 9
print(f"{x} ** 1/4 = {x ** (1/4)}")

xn = x
n = 0

while True:
    n += 1
    xn_1 = xn
    xn = 1/4 * (3 * xn + (x / (xn ** 3)))
    if abs(xn - xn_1) < 0.0001:
        break


print(f"{x} ** 1/4 = {xn} n = {n}")