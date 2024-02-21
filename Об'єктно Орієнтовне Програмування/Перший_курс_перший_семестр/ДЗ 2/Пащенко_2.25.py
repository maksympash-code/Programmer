a,b,c = [int(d) for d in input().split()]

if  a < b and a > c :
    print(c + b)
elif a > c and a > b and b > c:
    print(a + c)
elif a > c and a > b and b < c:
    print(a + b)
elif c > a and c > b:
    print(a + c)