# n=int(input01())
#
# for i in range(n+1,2):
#     if n%i == 0:
#         print(i)
#         break
# else:
#     print(n)

n=int(input())
counter=1
i=2

while i * i<n:
    if n%i==0:
        counter=n//i
        break
    else:
        i+=1
print(counter)