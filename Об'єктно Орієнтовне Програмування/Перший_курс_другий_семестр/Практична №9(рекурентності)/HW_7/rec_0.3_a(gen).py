def gen(n):
    res = 0
    yield res
    for i in range(1, n+1):
        res += 1 / (i * (i+1))
        yield res

n = int(input("Введіть член послідовності до якого хочете обчислити суму:"))

iter_for_gen = iter(gen(n))
if n >= 1:
    print(f"S_{n}: result = {next(iter_for_gen)}")
    print(f"S_{n}: result = {next(iter_for_gen)}")
    print(f"S_{n}: result = {next(iter_for_gen)}")
else:
    raise ValueError
