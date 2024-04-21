n = int(input("Введіть число члена,якого хочете обчислити:"))
x3 = 0
x2 = 1
x1 = 1

# x3
#    x2
#       x3
#          xn
# 0  1  1  1

for n in range(3,n + 1):
    xn = x1 + x3
    x3 = x2
    x2 = x1
    x1 = xn

print(x1)