# В матрице элементы второго столбца возвести в квадрат.

import random

# Генерируем случайную матрицу размером 4x4
n = 4  # количество строк
m = 4  # количество столбцов

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(-10, 10))
    matrix.append(row)

# Выводим исходную случайную матрицу
print("Исходная случайная матрица:")
for i in range(len(matrix)):
    print(matrix[i])

# Возводим в квадрат элементы второго столбца
for i in range(len(matrix)):
    matrix[i][1] = matrix[i][1] ** 2

print()
print("Матрица после возведения второго столбца в квадрат:")
for i in range(len(matrix)):
    print(matrix[i])