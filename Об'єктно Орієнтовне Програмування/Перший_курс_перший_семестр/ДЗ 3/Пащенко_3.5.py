n = int(input())
sum = 0
dob = 1
while n > 0:
    k = n % 10
    sum += k
    dob *= k
    n = n // 10
relation = dob / sum
print(f"{relation:0.3f}")