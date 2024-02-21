a, b, c,d = [float(d) for d in input().split()]

if a == c and b == d:
    print("YES")
elif a == b and c == d:
    print("YES")
elif a == d and b == c:
    print("YES")
else:
    print("NO")