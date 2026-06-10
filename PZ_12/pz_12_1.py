# В матрице найти сумму элементов второй половины матрицы.
# Исходная матрица

import random

# Генерируем случайную матрицу размером 4x4
n = 4  # количество строк
m = 4  # количество столбцов

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randint(1, 10))
    matrix.append(row)

print("Исходная случайная матрица:")
for i in range(len(matrix)):
    print(matrix[i])

n = len(matrix)  # количество строк
m = len(matrix[0])  # количество столбцов

print()
print("Размер матрицы:", n, "x", m)

# Определяем общее количество элементов
total_elements = n * m
half_elements = total_elements // 2

print("Всего элементов:", total_elements)
print("Элементов во второй половине:", half_elements)
print()

# Вторая половина (нижняя половина матрицы)
print()
print("Вторая половина матрицы:")
summa = 0
half = n // 2
for i in range(half, n):
    for j in range(m):
        summa = summa + matrix[i][j]
        print("Добавляем элемент", matrix[i][j])

print("Сумма элементов нижней половины матрицы:", summa)