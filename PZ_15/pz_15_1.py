import sqlite3 as sq
from data import initialize_database, DB_NAME

# Инициализируем базу данных (создаем файл и наполняем его)
initialize_database()

def print_table(cursor, title_text):
    """Функция для красивого вывода таблицы."""
    print('\n' + '=' * 110)
    print(title_text.center(110))
    print('=' * 110)
    print(f"{'ID':<4} {'ФИО Пациента':<28} {'ФИО Врача':<28} {'Диагноз':<22} {'Стоимость'}")
    print('-' * 110)
    
    cursor.execute("SELECT * FROM Patient ORDER BY id")
    for row in cursor.fetchall():
        id_, p_fio, d_fio, diag, cost = row
        print(f"{id_:<4} {p_fio:<28} {d_fio:<28} {diag:<22} {cost:>10.2f} руб.")

# Подключаемся к созданной базе данных для работы
with sq.connect(DB_NAME) as con:
    cursor = con.cursor()

    # Исходное состояние
    print_table(cursor, "Исходное содержимое таблицы Пациент")

    # 3 ЗАПРОСА
    print("\n1. Пациенты с стоимостью лечения более 20000 руб.:")
    cursor.execute("SELECT patient_fio, doctor_fio, treatment_cost FROM Patient WHERE treatment_cost > 20000")
    for row in cursor.fetchall():
        print(f" - {row[0]} (врач: {row[1]}) — {row[2]:.2f} руб.")

    print("\n2. Пациенты, у которых диагноз содержит 'ит' или 'грипп':")
    cursor.execute("""
        SELECT patient_fio, diagnosis 
        FROM Patient 
        WHERE diagnosis LIKE '%ит%' OR diagnosis LIKE '%грипп%'
    """)
    for row in cursor.fetchall():
        print(f" - {row[0]} (Диагноз: {row[1]})")

    print("\n3. Пациенты врача 'Петров Сергей Александрович':")
    cursor.execute("""
        SELECT patient_fio, diagnosis, treatment_cost 
        FROM Patient 
        WHERE doctor_fio = 'Петров Сергей Александрович'
    """)
    for row in cursor.fetchall():
        print(f" - {row[0]} ({row[1]}) — {row[2]:.2f} руб.")

    # РЕДАКТИРОВАНИЕ
    cursor.execute("UPDATE Patient SET treatment_cost = 32000.00 WHERE diagnosis = 'Пневмония'")
    cursor.execute("UPDATE Patient SET doctor_fio = 'Волков Михаил Юрьевич' WHERE patient_fio LIKE '%Сидорова%'")
    cursor.execute("UPDATE Patient SET diagnosis = 'Хронический гастрит' WHERE diagnosis = 'Гастрит'")

    print_table(cursor, "Таблица после 3-х операций редактирования")

    # УДАЛЕНИЕ
    cursor.execute("DELETE FROM Patient WHERE treatment_cost < 7000")
    cursor.execute("DELETE FROM Patient WHERE patient_fio LIKE '%Морозов%'")
    cursor.execute("DELETE FROM Patient WHERE id = 9")

    print_table(cursor, "Итоговая таблица после 3-х операций удаления")

print("\n Демонстрация работы базы данных 'Платная поликлиника' завершена!")