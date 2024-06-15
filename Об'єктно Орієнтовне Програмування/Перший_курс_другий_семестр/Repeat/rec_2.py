def rec(x,k):
    if k >= 1:
        return (((-1)**k) * x**k) / k
    else:
        raise ValueError

x = float(input("Введіть будь яке число:"))
k = int(input("Введіть k >= 1: "))
print(rec(x,k))