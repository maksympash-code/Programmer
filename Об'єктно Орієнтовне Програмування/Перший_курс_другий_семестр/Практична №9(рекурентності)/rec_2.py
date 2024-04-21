n = int(input("Введіть номер послідовності, що хочете обчислити:"))
x = float(input("x = "))

a = x
for k in range (2,n+1):
    a += (1/k)

print(a)