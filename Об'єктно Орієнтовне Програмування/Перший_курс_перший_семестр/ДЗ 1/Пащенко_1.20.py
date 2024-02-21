x, y = [float(d) for d in input().split()]

v1 = ((x**2 + y**2)**0.5) / (x - y)**2
v2 = (2 * x * y) / (x**2 + y**2)**0.5

print(f"{v1 - v2:0.3f}")