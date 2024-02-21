# n = int(input())
# i=1
# while i ** 3 < n:
#     print(i**3,end=" ")
#     i+=1

n = int(input())

kub=1

for i in range(int(n**(1/3))):
    print(kub**3, end=" ")
    kub+=1