a, b, c = [int(d) for d in input().split()]

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("YES")
else:
    print("NO")