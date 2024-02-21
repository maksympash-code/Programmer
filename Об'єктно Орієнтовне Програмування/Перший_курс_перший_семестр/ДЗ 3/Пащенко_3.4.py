n = int(input())

counter = 0
while n > 0:
    k = n % 10
    if k != 0:
        counter += 1
    n = n // 10
print(counter)