def Bin(n: int):
    lst = []
    while n != 0:
        k = n % 2
        lst.append(str(k))
        n //= 2
    lst = lst[::-1]
    return lst


n , k = [int(el) for el in input().split()]
counter=0

for i in range(n,k+1):
    n = Bin(i)
    for j in range(len(n)):
        if int(n[j]) == 1:
            counter+=1
print(counter)

