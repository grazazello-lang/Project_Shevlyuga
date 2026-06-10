import random

# Создаём два исходных текстовых файла
# Генерируем по 8 случайных чисел в диапазоне от -50 до 50 и объединяем их в строку
l1 = [' '.join(str(random.randint(-50, 50)) for _ in range(8))]
f1 = open('file1.txt', 'w')
f1.writelines(l1)
f1.close()

l2 = [' '.join(str(random.randint(-50, 50)) for _ in range(8))]
f2 = open('file2.txt', 'w')
f2.writelines(l2)
f2.close()

# Читаем файлы и преобразуем строку в список чисел
f1 = open('file1.txt')
k1 = f1.read()
k1 = k1.split()
for i in range(len(k1)):
    k1[i] = int(k1[i])
f1.close()

f2 = open('file2.txt')
k2 = f2.read()
k2 = k2.split()
for i in range(len(k2)):
    k2[i] = int(k2[i])
f2.close()

# Объединяем элементы из двух файлов в один список
all_elements = k1 + k2

# Сортируем объединенный список
sorted_elements = sorted(all_elements)

# Количество элементов
count_elements = len(sorted_elements)

# Поиск минимального элемента, кратного 2
min_multiple_2 = None
for i in range(len(sorted_elements)):
    if sorted_elements[i] % 2 == 0:
        min_multiple_2 = sorted_elements[i]
        break

# Поиск максимального элемента, кратного 5
max_multiple_5 = None
for i in range(len(sorted_elements) - 1, -1, -1):
    if sorted_elements[i] % 5 == 0:
        max_multiple_5 = sorted_elements[i]
        break

# Записываем результат в файл
f3 = open('result.txt', 'w', encoding='UTF-8')
f3.write('Элементы первого и второго файлов: ')
f3.write('\n')
f3.write(str(all_elements))
f3.write('\n')
f3.write('Элементы после сортировки: ')
f3.write('\n')
f3.write(str(sorted_elements))
f3.write('\n')
f3.write('Количество элементов: ')
f3.write(str(count_elements))
f3.write('\n')
f3.write('Минимальный элемент кратный 2: ')
f3.write(str(min_multiple_2))
f3.write('\n')
f3.write('Максимальный элемент кратный 5: ')
f3.write(str(max_multiple_5))
f3.close()

print("Результат записан в файл result.txt")