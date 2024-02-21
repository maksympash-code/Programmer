n = int(input())
i = 1
k = 1

if n == 0:
    print(k)
elif n != 0:
    while True:
        k *= i
        if i == n:
            break
        i += 1
    print(k)