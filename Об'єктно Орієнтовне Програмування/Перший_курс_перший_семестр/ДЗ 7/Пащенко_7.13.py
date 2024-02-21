def dif(n):
    lst = []
    for i in range(len(str(n))):
        c = n % 10
        if c not in lst:
            lst.append(c)
        else:
            return False
        n = n // 10

    return True


a, b = [int(d) for d in input().split()]

for i in range(a, b+1):
    if dif(i):
        print(i, end = " ")