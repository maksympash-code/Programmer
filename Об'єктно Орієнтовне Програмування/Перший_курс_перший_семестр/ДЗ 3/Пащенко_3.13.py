n = int(input())

i = 0
fact = 1
k = 0
while fact < n:
    k += 1
    i += 1
    fact *= i

print(k)