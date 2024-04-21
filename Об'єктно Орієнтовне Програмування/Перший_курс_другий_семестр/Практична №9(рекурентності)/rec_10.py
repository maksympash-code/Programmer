# x = int(input())
# k = 0
# x0 = x / 2
#
# while abs (x0) >= 0.00001:
#     k += 1
#     x0 = 1/2 * (x0 + (x / x0))
#
# print(x0)

x = 20
print(f"{x} ** 0.5 = {x ** 0.5}")

xn = x
n = 0

while True:
    n += 1
    xn = 0.5 * (xn + (x / xn))
    if abs(xn ** 2 - x) < 0.0001:
        break


print(f"{x} ** 0.5 = {xn} n ={n}")