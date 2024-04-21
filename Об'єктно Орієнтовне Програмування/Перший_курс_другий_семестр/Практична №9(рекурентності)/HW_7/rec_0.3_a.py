def rec(n):
    res = 0
    for i in range(1, n+1):
        res += 1 / (i * (i+1))
    return res

n = int(input("Введіть член послідовності до якого хочете обчислити суму:"))
if n >= 1:
    print(f"S_{n}: result = {rec(n)}")
else:
    raise ValueError
