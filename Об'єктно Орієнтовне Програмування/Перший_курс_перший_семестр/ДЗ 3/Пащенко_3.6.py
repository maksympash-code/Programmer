n = int(input())
row = ""

while n > 0:
    k = n % 10
    row += str(k)
    n = n // 10

print(row)