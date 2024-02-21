n = int(input())

k = 0
i = 1
j = n


if n == 0:
    print(1)

while j > 0:
    j = j // 10
    k += 1

while k > 0:
    i = n // 10**(k-1)
    n -= i*10**(k-1)
    k -= 1

    if i % 2 == 1:
        print(i - 1, end = "")
    elif i % 2 == 0:
        print(i + 1, end = "")