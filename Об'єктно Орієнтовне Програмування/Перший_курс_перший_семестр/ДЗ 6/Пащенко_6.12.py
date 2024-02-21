a = input()
k=int(input())

b=""

for syb in a:
    if ord(syb)-k < 65:
        s=(ord(syb)-k)+26
        b+=chr(s)
    elif 65 <=ord(syb)-k <= 90:
        s=ord (syb) - k
        b+=chr(s)
print(b)
