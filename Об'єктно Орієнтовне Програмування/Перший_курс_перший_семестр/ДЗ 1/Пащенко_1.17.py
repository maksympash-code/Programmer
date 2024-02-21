a, b, c = [int(d) for d in input().split()]
p1 = (a + b + c) / 2

S = (p1 * (p1 - a) * (p1 - b) * (p1 - c))**0.5

ha = (2 * S)/a
hb = (2 * S)/b
hc = (2 * S)/c

print(f"{ha:0.2f}",f"{hb:0.2f}",f"{hc:0.2f}")