# Даны два списка A и B одинакового размера N. Сформировать новый список C того
# же размера, каждый элемент которого равен максимальному из элементов списков
# A и B.

import random

try:
    N = int(input("Введите размер списков: "))
    if N >= 0:
        A = [random.randint(1, 100) for _ in range(N)]
        B = [random.randint(1, 100) for _ in range(N)]

        C = [max(A[i], B[i]) for i in range(N)]

        print(f"Список A: {A}")
        print(f"Список B: {B}")
        print(f"Список C: {C}")
    else:
        print("Введите положительное число!")
except ValueError:
    print("Введите корректное число!")