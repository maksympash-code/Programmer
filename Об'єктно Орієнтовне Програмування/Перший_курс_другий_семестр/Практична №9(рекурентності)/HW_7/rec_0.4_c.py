n = int(input("Вкажіть порядок визначника, що хочете знайти:"))

D2 = 3 # D_1 D_n-2
D1 = 7 # D_2 D_n-1

# D2
#    D1
#       D
# 3  7  15

for i in range(3,n+1):
    D = 3 * D1 - 2 * D2
    D2 = D1
    D1 = D

print(D)

