a, b, c = [int(d) for d in input().split()]

if a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)
elif b < a < c or c < a < b:
    print(a)