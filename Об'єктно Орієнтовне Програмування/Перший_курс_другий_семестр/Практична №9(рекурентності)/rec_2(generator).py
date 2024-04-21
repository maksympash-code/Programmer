def gen():
    a = 1
    n = 1
    yield a,n
    while True:
        n += 1
        a += 1/n # цей генаратор буде генерувати нескінченну послідовність
        yield a,n

for a,n in gen():
    print(a,n)
    if a > 10:
        break