from math import *

def f(x):
    return (1/2) * sin(x + 1)

n = int(log(10 ** 8 * sin (1), 2) + 1)
print(n)

x0 = 0
x1 = f(x0)
# while n > 0:
#     n -= 1
#     x0 = x1
#     x1 = f(x0)

for i in range(1, n + 1):
     x0 = x1
     x1 = f(x0)

print(x1)
