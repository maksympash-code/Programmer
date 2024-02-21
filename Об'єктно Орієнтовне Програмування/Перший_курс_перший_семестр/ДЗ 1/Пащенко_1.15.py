n = abs(int(input()))
if 99 < n < 1000:
    sum = n//100 + n // 10 % 10 + n % 10
    dob = (n//100) * (n // 10 % 10) * (n % 10)
    print(dob - sum)