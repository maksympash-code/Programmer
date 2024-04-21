def rec(n):
    res = 0
    for i in range(2,n+2):
        res += (((-1)**i) * (i - 1)) / i
    return res

n = int(input("Введіть член послідовності до якого хочете обчислити суму:"))
if n >= 1:
    print(f"S_{n}: result = {rec(n)}")
else:
    raise ValueError
