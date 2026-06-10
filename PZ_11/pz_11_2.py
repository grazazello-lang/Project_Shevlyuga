# Составить генератор (yield), который выводит из строки только цифры.

# Генератор, который выводит из строки только цифры
def digit_generator(s):
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            yield s[i]

# Пример использования
text = "abc123def456ghi789"
print("Исходная строка:", text)

print("Цифры из строки:", end=" ")
for digit in digit_generator(text):
    print(digit, end="")