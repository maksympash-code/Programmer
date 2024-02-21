n = int(input())

summa = 0
f=0
while n > 0:
    last_digit = n % 10
    if last_digit % 2 ==0:
        summa += last_digit
        f=1
    n = n // 10
if f==1:
    print(summa)
else:
    print(-1)
