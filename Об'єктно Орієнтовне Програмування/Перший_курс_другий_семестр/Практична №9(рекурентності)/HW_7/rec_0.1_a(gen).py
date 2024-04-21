import math

def gen(n):
    res = 0
    yield res
    for k in range(1,n+1):
        res = math.sqrt(2 + res)
        yield res


n = int(input("Введіть кількість коренів яку хочете обчислити:"))
print(math.sqrt(2 + math.sqrt(2))) # виводить результат для перевірки

iter_for_gen = iter(gen(2))

print(next(iter_for_gen))
print(next(iter_for_gen))
print(next(iter_for_gen))