n = int(input())
x0 = 1
x1 = 1

# x0
#    x1
#       x2
# 1  1 + 1/1

for i in range(1,n+1):
    xn = x0 + 1 / x1
    x1 = xn

print(xn)