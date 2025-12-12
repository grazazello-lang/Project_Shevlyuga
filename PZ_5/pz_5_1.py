# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m.
# Суммирование оформить функцией с параметрами.
# Значения n и m программа должна запрашивать.

def sum_range(n, m):
    total = 0
    i = n
    while i <= m:
        total += i
        i += 1
    return total
try:
    n = int(input("Введите начальное число n: "))
    m = int(input("Введите конечное число m: "))

    if n > m:
        print("Ошибка: n должно быть меньше или равно m")
    else:
        result = sum_range(n, m)
        print(f"Сумма чисел от {n} до {m} включительно: {result}")
except ValueError:
    print("Введите корректное значение!")
