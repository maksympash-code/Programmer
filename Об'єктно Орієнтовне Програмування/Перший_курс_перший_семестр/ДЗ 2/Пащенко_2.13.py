a, b, c = [int(d) for d in input().split()]

if a==b==c:
    print(1)
elif a!=b and b!=c and a!=c:
    print(3)
elif a==b or b==c or a==c:
    print(2)