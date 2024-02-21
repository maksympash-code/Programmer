a, b, c, d, f = [float(d) for d in input().split()]
p1 = (a + b + f) / 2
g1 = (p1 * (p1-a) * (p1-b) * (p1-f)) ** 0.5

p2 = (c + d + f) / 2
g2 = (p2 * (p2-c) * (p2-d) * (p2-f)) ** 0.5

G = g1 + g2
print(f"{G:0.4f}")