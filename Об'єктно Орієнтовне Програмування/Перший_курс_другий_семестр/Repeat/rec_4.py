n = int(input())
S_n = 0

for i in range(1,n+1):
    S_n += (-1)**(i-1) * (i / (i + 1))

print(S_n)