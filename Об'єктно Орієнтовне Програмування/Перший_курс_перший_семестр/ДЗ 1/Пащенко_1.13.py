x , y =[float(d) for d in input().split()]

v1 = (x ** 2 - 2 *x * y + 4 * (y**2)) / (x + 5)
v2 = (3 * (x**2) - y ** 2) / (y - 7)
print(f"{v1+v2:0.3f}")