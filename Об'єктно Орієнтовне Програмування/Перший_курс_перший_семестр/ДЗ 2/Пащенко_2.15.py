a, b, c = [int(d) for d in input().split()]

D = b**2 - 4 * a * c
if D > 0:
    x1 = int((-b + D**0.5) / (2*a))
    x2 = int((-b - D**0.5) / (2*a))
    if x1 > x2:
        print("Two roots:",x2,x1)
    elif x2 > x1:
        print("Two roots:",x1,x2)
elif D == 0:
    x = int(-b / (2 * a))
    print("One root:", x)
else:
    print("No roots")