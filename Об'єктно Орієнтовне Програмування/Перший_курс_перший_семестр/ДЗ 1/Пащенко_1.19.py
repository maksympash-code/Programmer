x1, y1 = [int(d) for d in input().split()]
x2, y2 = [int(d) for d in input().split()]
n = int(input())

A = x2 - x1
B = y2 - y1

dov = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

nor_1 = A / dov
nor_2 = B / dov

nor_1_n = (A / dov) * 5
nor_2_n = (B / dov) * 5

print(f"{A: 0.9f}", f"{B: 0.9f}")
print(f"{nor_1: 0.9f}", f"{nor_2: 0.9f}")
print(f"{nor_1_n: 0.9f}", f"{nor_2_n: 0.9f}")
if  A >= 0 and B >= 0:
    print(f"{B: 0.9f}", f"{-A: 0.9f}")
elif A>=0 and B<=0:
    print(f"{-A: 0.9f}", f"{B: 0.9f}")
elif A<=0 and B<=0:
    print(f"{A: 0.9f}", f"{-B: 0.9f}")