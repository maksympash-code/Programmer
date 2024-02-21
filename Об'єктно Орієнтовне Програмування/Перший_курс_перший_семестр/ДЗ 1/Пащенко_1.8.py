a = int(input())
if a > 0 and 99<a<1000:
    print((a// 100) * (a//10 %10) * (a%10))