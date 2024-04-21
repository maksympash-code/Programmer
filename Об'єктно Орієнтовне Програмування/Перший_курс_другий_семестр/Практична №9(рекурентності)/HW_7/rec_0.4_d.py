n = int(input("Вкажіть порядок визначника, що хочете знайти:"))

D2 = 0 # D_1 D_n-1
D1 = 1 # D_2 D_n-2
# D2
#    D1
#       D
# 0  1  0  -1

for i in range(2,n+1):
    D = 0 * D1 - 1 * D2
    D2 = D1
    D1 = D

print(D)

