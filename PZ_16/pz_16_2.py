# Базовый класс для всех типов автомобилей
class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Автомобиль: {self.make} {self.model}, Год выпуска: {self.year}"


# Класс Грузовик, наследуемый от Автомобиля
class Truck(Car):
    def __init__(self, make: str, model: str, year: int, payload: float):
        # Вызываем конструктор родительского класса для инициализации общих полей
        super().__init__(make, model, year)
        self.payload = payload

    def __str__(self):
        # Получаем базовую строку из родительского класса и дополняем её
        base_info = super().__str__()
        return f"{base_info}, Тип: Грузовик, Грузоподъемность: {self.payload} т"


# Класс Легковой автомобиль, наследуемый от Автомобиля
class PassengerCar(Car):
    def __init__(self, make: str, model: str, year: int, passengers: int):
        # Вызываем конструктор родительского класса
        super().__init__(make, model, year)
        self.passengers = passengers

    def __str__(self):
        # Получаем базовую строку из родительского класса и дополняем её
        base_info = super().__str__()
        return f"{base_info}, Тип: Легковой, Количество пассажиров: {self.passengers}"


# === Демонстрация работы классов ===
if __name__ == "__main__":
    # Создаем экземпляр базового класса
    auto = Car("Неизвестная марка", "Модель X", 2020)
    
    # Создаем экземпляр грузовика
    truck = Truck("КАМАЗ", "6520", 2022, 20.0)
    
    # Создаем экземпляр легкового автомобиля
    car = PassengerCar("Toyota", "Camry", 2023, 5)

    # Выводим информацию о каждом объекте (автоматически вызывается метод __str__)
    print(auto)
    print(truck)
    print(car)
    
    # Демонстрация доступа к отдельным атрибутам
    print(f"\nПроверка атрибутов грузовика: Марка - {truck.make}, Грузоподъемность - {truck.payload} т")