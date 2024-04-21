def gen(n):
    res = 0
    yield res
    for i in range(2,n+1):
        res += ((-1)**i * (i-1)) / i
        yield res

n = int(input("Введіть член послідовності до якого хочете обчислити суму:"))

iter_for_gen = iter(gen(n))
if n >= 2:
    print(next(iter_for_gen))
    print(next(iter_for_gen))
    print(next(iter_for_gen))
else:
    raise StopIteration