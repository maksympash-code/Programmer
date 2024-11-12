from time import *
from functools import lru_cache

@lru_cache
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

start = perf_counter()
print(fib(500))
end = perf_counter()
print(f"Стільки часу рахує число Фібоначі: {end - start}")