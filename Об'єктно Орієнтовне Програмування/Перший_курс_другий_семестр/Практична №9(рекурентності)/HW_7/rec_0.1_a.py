import math

n = int(input("Введіть кількість коренів яку хочете обчислити:"))
print(math.sqrt(2 + math.sqrt(2)))
res = 0

for k in range(n):
    res = math.sqrt(2 + res)

print(res)