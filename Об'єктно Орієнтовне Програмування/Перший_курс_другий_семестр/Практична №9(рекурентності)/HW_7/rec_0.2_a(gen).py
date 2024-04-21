def gen(x , k):
    yield x,k
    x = x ** k / k
    yield x,k

x = float(input())
k = int(input())
iter_for_gen = iter(gen(x,k))

if k >= 1:
    print(next(iter_for_gen))
    print(next(iter_for_gen))

else:
    raise ValueError