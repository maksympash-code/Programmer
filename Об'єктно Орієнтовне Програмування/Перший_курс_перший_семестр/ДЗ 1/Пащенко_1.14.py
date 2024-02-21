x , y =[float(d) for d in input().split()]

v1 = (2 * x * y) / ((x**2 + y**2)**0.5)
v2 = (x + y - 1)**2 / (x * y)
print(f"{v1-v2:0.3f}")