n = int(input())

if n % 2 != 0 or n > 0 and 100 <= n <= 999:
    print("YES")
else:
    print("NO")