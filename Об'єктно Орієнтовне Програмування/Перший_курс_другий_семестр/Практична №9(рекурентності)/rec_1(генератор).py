def gen(n,x):
    a = x  # a - поточний член нашої послідовності
    yield a # повертаємо найперший член послідовності
    for k in range(1, n + 1):
        # a = - (x ** 2) / ((2*k) * (2*k+1)) * a
        a *= - (x ** 2) / ((2 * k) * (2 * k + 1))
        yield a # повертаємо наступний згенерований член послідовності



n = int(input("ВВедіть номер послідовності, що хочете обчислити:"))
x = float(input("x = "))

# for a in gen(n,x):
#     print(a)
# l = list(gen(4,1))
# print(l)

iter_for_gen = iter (gen(4,5))
print(next(iter_for_gen))
print(next(iter_for_gen))
print(next(iter_for_gen))
