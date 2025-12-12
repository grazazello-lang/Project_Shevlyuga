# Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
# положительного числа K, а также их сумму S (K — входной, C и S — выходные
# параметры целого типа). С помощью этой функции найти количество и сумму цифр
# для каждого из пяти данных целых чисел.

def DigitCountSum(K, C, S):
    C = 0
    S = 0
    temp = K

    if temp == 0:
        C = 1
        S = 0
        return C, S

    while temp > 0:
        digit = temp % 10
        S += digit
        C += 1
        temp //= 10
    return C, S

try:
    K = int(input("Введите число #1: "))
    C, S = DigitCountSum(K, 0, 0)
    print(f"Количество цифр: {C}, Сумма цифр: {S}")
except ValueError:
    print("Введите корректное число!")
try:
    K = int(input("Введите число #2: "))
    C, S = DigitCountSum(K, 0, 0)
    print(f"Количество цифр: {C}, Сумма цифр: {S}")
except ValueError:
    print("Введите корректное число!")
try:
    K = int(input("Введите число #3: "))
    C, S = DigitCountSum(K, 0, 0)
    print(f"Количество цифр: {C}, Сумма цифр: {S}")
except ValueError:
    print("Введите корректное число!")
try:
    K = int(input("Введите число #4: "))
    C, S = DigitCountSum(K, 0, 0)
    print(f"Количество цифр: {C}, Сумма цифр: {S}")
except ValueError:
    print("Введите корректное число!")
try:
    K = int(input("Введите число #5: "))
    C, S = DigitCountSum(K, 0, 0)
    print(f"Количество цифр: {C}, Сумма цифр: {S}")
except ValueError:
    print("Введите корректное число!")