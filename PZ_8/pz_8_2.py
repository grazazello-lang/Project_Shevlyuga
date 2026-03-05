# Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая средние
# температуры по месяцам в году. Преобразовать информацию из строки в словарь, с
# использованием функции найти среднюю и минимальные температуры, результаты
# вывести на экран.

data_string = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
parts = data_string.split()

year = parts[0]
temperatures = list(map(int, parts[1:]))

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Окторябрь', 'Ноябрь', 'Декабрь']

temperature_dict = {}
for i in range(len(months)):
    temperature_dict[months[i]] = temperatures[i]

temperature_dict['Год'] = year

def calculate_average(temp_list):
    return sum(temp_list) / len(temp_list)

def find_min(temp_list):
    return min(temp_list)

avg_temp = calculate_average(temperatures)
min_temp = find_min(temperatures)

print("Словарь с температурами по месяцам:")
for month, temp in temperature_dict.items():
    if month != 'Год':
        print(f"{month}: {temp}°C")
    else:
        print(f"Год: {temp}")

print(f"\nСредняя температура за год: {avg_temp:.1f}°C")
print(f"Минимальная температура за год: {min_temp}°C")
