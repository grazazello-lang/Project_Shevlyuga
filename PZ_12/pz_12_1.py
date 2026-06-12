# В матрице найти сумму элементов второй половины матрицы.
# Исходная матрица

import random

# Генерируем случайную матрицу размером 4x4
n = int(input("Введите количество строк: "))  # количество строк
m = int(input("Введите количество столбцов: "))  # количество столбцов

matrix = [[random.randint(1, 10) for j in range(m)] for i in range(n)]

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

half = n // 2

second_half_elements = [matrix[i][j] for i in range(half, n) for j in range(m)]

list(map(lambda x: print("Добавляем элемент", x), second_half_elements))

summa = sum(second_half_elements)

print("Сумма элементов нижней половины матрицы:", summa)