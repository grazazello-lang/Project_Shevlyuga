# Даны числа х, у. Проверить истинность высказывания:
# «Точка с координатами (х, у) лежит во второй координатной четверти».
while True:
    try:
        x = float(input("Введите координату x: "))
        y = float(input("Введите координату y: "))
        break
    except ValueError:
        print("Ошибка, введите числa для координат!")

coordinates = (x < 0) and (y > 0)
if coordinates == False:
    coordinates = "Нет"
else:
    coordinates = "Да"

print(f"Точка с координатами ({x}, {y}) лежит во второй координатной четверти: {coordinates}")