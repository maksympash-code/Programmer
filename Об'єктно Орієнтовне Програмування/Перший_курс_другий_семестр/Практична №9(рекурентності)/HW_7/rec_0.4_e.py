n = int(input("Вкажіть порядок визначника, що хочете знайти:"))
a = int(input("Введіть будь яке число:"))
D1 = a
D2 = a ** 2 - 1
D3 = a ** 3 - 2 * a

for i in range(4,n+1):
    D = D1 * D3 - D2
    D2 = D3
    D3 = D

print(D)