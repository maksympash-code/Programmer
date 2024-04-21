n = int(input())
# x0 = 2
# x1 = 2.5

x0 = 1
x1 = 1 + 1/2


# for i in range(1,n+1):
#     xn = x0 + 1 / x1
#     x1 = xn

for i in range(1 , 1+n):
    xn = x0 + 1 / (2 + (x1 - 1))
    x1 = xn

print(xn)