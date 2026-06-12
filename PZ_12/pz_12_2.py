# В матрице элементы второго столбца возвести в квадрат.

import random

# Генерируем случайную матрицу размером 4x4
n = 4  # количество строк
m = 4  # количество столбцов

matrix = [[random.randint(-10, 10) for j in range(m)] for  i in range(n)]


# Выводим исходную случайную матрицу
print("Исходная случайная матрица:")
list(map(print, matrix))

# Возводим в квадрат элементы второго столбца
qvadrat = [[row[j] ** 2 if j == 1 else row[j] for j in range(len(row))] for row in matrix]

print()
print("Матрица после возведения второго столбца в квадрат:")
list(map(print, matrix))