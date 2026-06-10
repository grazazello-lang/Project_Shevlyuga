# Приложение ПЛАТНАЯ ПОЛИКЛИНИКА для некоторой организации. БД
# должна содержать таблицу Пациент со следующей структурой записи: ФИО пациента,
# ФИО врача, диагноз, стоимость лечение.
import sqlite3
import sys

DB_NAME = "paid_clinic.db"


def init_db(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patient (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_fio TEXT NOT NULL,
            doctor_fio TEXT NOT NULL,
            diagnosis TEXT NOT NULL,
            treatment_cost REAL NOT NULL
        )
    ''')
    conn.commit()


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное числовое значение.")


def input_10_records(conn):
    # Ввод 10 записей в БД.
    cursor = conn.cursor()
    print("\n📝 ВВОД 10 ПОЗИЦИЙ В БАЗУ ДАННЫХ")
    for i in range(1, 11):
        print(f"--- Запись {i}/10 ---")
        p_fio = input("ФИО пациента: ").strip()
        d_fio = input("ФИО врача: ").strip()
        diag = input("Диагноз: ").strip()
        cost = get_float_input("Стоимость лечения: ")

        cursor.execute('''
            INSERT INTO Patient (patient_fio, doctor_fio, diagnosis, treatment_cost)
            VALUES (?, ?, ?, ?)
        ''', (p_fio, d_fio, diag, cost))
    conn.commit()
    print("10 записей успешно добавлены.")


def display_all(conn):
    # Вывод всех записей для контроля.
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Patient ORDER BY id")
    rows = cursor.fetchall()
    if not rows:
        print("База данных пуста.")
        return

    print(f"\n{'ID':<4} | {'ФИО Пациента':<20} | {'ФИО Врача':<20} | {'Диагноз':<15} | {'Стоимость':<10}")
    print("-" * 80)
    for r in rows:
        print(f"{r[0]:<4} | {r[1]:<20} | {r[2]:<20} | {r[3]:<15} | {r[4]:<10.2f} руб.")


# ПОИСК (3 SQL-запроса)
def search_records(conn):
    print("\n ПОИСК ЗАПИСЕЙ")
    print("1. По ФИО пациента (точное совпадение)")
    print("2. По диагнозу (частичное совпадение)")
    print("3. По стоимости лечения (больше указанной)")
    choice = input("Выберите вариант (1-3): ").strip()

    cursor = conn.cursor()
    if choice == '1':
        fio = input("Введите ФИО пациента: ").strip()
        # SQL-запрос 1
        cursor.execute("SELECT * FROM Patient WHERE patient_fio = ?", (fio,))
    elif choice == '2':
        diag = input("Введите часть диагноза: ").strip()
        # SQL-запрос 2
        cursor.execute("SELECT * FROM Patient WHERE diagnosis LIKE ?", (f"%{diag}%",))
    elif choice == '3':
        cost = get_float_input("Минимальная стоимость: ")
        # SQL-запрос 3
        cursor.execute("SELECT * FROM Patient WHERE treatment_cost > ?", (cost,))
    else:
        print("Неверный выбор.")
        return

    results = cursor.fetchall()
    if results:
        display_all(conn)  # Переиспользуем форматированный вывод
    else:
        print("Записи не найдены.")


# УДАЛЕНИЕ (3 SQL-запроса)
def delete_records(conn):
    print("\nУДАЛЕНИЕ ЗАПИСЕЙ")
    print("1. По ФИО пациента")
    print("2. По диагнозу")
    print("3. По стоимости лечения (меньше или равно указанной)")
    choice = input("Выберите вариант (1-3): ").strip()

    cursor = conn.cursor()
    if choice == '1':
        fio = input("Введите ФИО пациента для удаления: ").strip()
        # SQL-запрос 1
        cursor.execute("DELETE FROM Patient WHERE patient_fio = ?", (fio,))
    elif choice == '2':
        diag = input("Введите диагноз для удаления: ").strip()
        # SQL-запрос 2
        cursor.execute("DELETE FROM Patient WHERE diagnosis = ?", (diag,))
    elif choice == '3':
        cost = get_float_input("Удалить записи со стоимостью <=: ")
        # SQL-запрос 3
        cursor.execute("DELETE FROM Patient WHERE treatment_cost <= ?", (cost,))
    else:
        print("Неверный выбор.")
        return

    conn.commit()
    print(f"Удалено строк: {cursor.rowcount}")


# РЕДАКТИРОВАНИЕ (3 SQL-запроса)
def edit_records(conn):
    print("\nРЕДАКТИРОВАНИЕ ЗАПИСЕЙ")
    print("1. Изменить стоимость лечения по ФИО пациента")
    print("2. Изменить диагноз по ФИО врача")
    print("3. Изменить ФИО врача по диагнозу")
    choice = input("Выберите вариант (1-3): ").strip()

    cursor = conn.cursor()
    if choice == '1':
        fio = input("ФИО пациента: ").strip()
        new_cost = get_float_input("Новая стоимость: ")
        # SQL-запрос 1
        cursor.execute("UPDATE Patient SET treatment_cost = ? WHERE patient_fio = ?", (new_cost, fio))
    elif choice == '2':
        doc = input("ФИО врача: ").strip()
        new_diag = input("Новый диагноз: ").strip()
        # SQL-запрос 2
        cursor.execute("UPDATE Patient SET diagnosis = ? WHERE doctor_fio = ?", (new_diag, doc))
    elif choice == '3':
        diag = input("Диагноз: ").strip()
        new_doc = input("Новое ФИО врача: ").strip()
        # SQL-запрос 3
        cursor.execute("UPDATE Patient SET doctor_fio = ? WHERE diagnosis = ?", (new_doc, diag))
    else:
        print("Неверный выбор.")
        return

    conn.commit()
    print(f"Обновлено строк: {cursor.rowcount}")


def main():
    # Подключение к БД (файл создаётся автоматически в папке со скриптом)
    conn = sqlite3.connect(DB_NAME)
    init_db(conn)

    while True:
        print("\n" + "=" * 40)
        print("ПЛАТНАЯ ПОЛИКЛИНИКА")
        print("=" * 40)
        print("1. Ввести 10 записей")
        print("2. Показать все записи")
        print("3. Поиск")
        print("4. Удаление")
        print("5. Редактирование")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            input_10_records(conn)
        elif choice == '2':
            display_all(conn)
        elif choice == '3':
            search_records(conn)
        elif choice == '4':
            delete_records(conn)
        elif choice == '5':
            edit_records(conn)
        elif choice == '0':
            print("Завершение работы. Соединение закрыто.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

    conn.close()


if __name__ == "__main__":
    main()