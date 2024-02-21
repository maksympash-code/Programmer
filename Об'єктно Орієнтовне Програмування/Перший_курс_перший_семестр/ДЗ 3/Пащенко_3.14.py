from math import *

n = int(input())

i = 0
summa = 1

while i < n:
    i += 1
    summa *= i

summa_1 = log10(summa) + 1

print(int(summa_1))