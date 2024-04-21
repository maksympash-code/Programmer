x = 9
print(f"{x} ** 1/3 = {x ** (1/3)}")

xn = x
n = 0

while True:
    n += 1
    xn_1 = xn
    xn = 1/3 * (2 * xn + (x / (xn ** 2)))
    if abs(xn - xn_1) < 0.0001:
        break


print(f"{x} ** 1/3 = {xn} n ={n}")