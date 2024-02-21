n = int(input())
od = n % 10
co = n // 100


if 99<n<1000 and od == co:
    print("=")
elif 99<n<1000:
    print(max(od,co))