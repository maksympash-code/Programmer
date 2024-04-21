def determinant_a(matrix, a):
    n = len(matrix)
    # Базовий випадок: для матриці 1x1 визначник це просто цей єдиний елемент
    if n == 1:
        return matrix[0][0]
    det = 0
    for j in range(n):
        # Обчислюємо мінор матриці
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        # Обчислюємо визначник рекурсивно для мінора і множимо на відповідний коефіцієнт
        det += ((-1) ** j) * matrix[0][j] * determinant_a(minor, a)
    return a * det

# Задаємо параметр a та розмір матриці
a = 1
n = 5

# Створюємо матрицю
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    matrix[i][i] = a
    if i > 0:
        matrix[i][i-1] = 1

# Обчислюємо визначник
det = determinant_a(matrix, a)
print("Determinant:", det)
