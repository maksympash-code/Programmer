x1, y1, x2, y2, a = [float(d) for d in input().split()]

x = (x1 + x2 * a) / (a+1)
y = (y1 + y2 * a) / (a+1)

print(f"{x:0.2f}",f"{y:0.2f}")