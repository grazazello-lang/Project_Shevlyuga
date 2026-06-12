# Приложение ПЛАТНАЯ ПОЛИКЛИНИКА для
# некоторой организации. БД должна содержать таблицу Пациент со следующей
# структурой записи: ФИО пациента, ФИО врача, диагноз, стоимость лечение.
import sqlite3 as sq
from data import patients_data

with sq.connect('polyclinic.db') as con:
    cursor = con.cursor()

    cursor.execute("DROP TABLE IF EXISTS Пациент")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Пациент (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio_patient TEXT NOT NULL,
        fio_doctor TEXT NOT NULL,
        diagnosis TEXT NOT NULL,
        cost REAL NOT NULL
    )""")

    cursor.executemany("INSERT INTO Пациент VALUES (NULL, ?, ?, ?, ?)", patients_data)

    def print_table(title_text):
        print('\n', title_text)
        print(f"{'ID':<4} {'ФИО пациента':<22} {'ФИО врача':<22} {'Диагноз':<25} {'Стоимость'}")
        cursor.execute("SELECT * FROM Пациент ORDER BY id")
        for row in cursor.fetchall():
            id_, fio_p, fio_d, diag, cost = row
            print(f"{id_:<4} {fio_p:<22} {fio_d:<22} {diag:<25} {cost:<10.2f}")

    print_table("Исходное содержимое таблицы Пациент")

    print("\n 1. Пациенты со стоимостью лечения более 10000:")
    cursor.execute("SELECT fio_patient, diagnosis, cost FROM Пациент WHERE cost > 10000")
    for row in cursor.fetchall():
        print(f" - {row[0]} ({row[1]}) - {row[2]:.2f} руб.")

    print("\n 2. Пациенты с воспалительными заболеваниями (гастрит или бронхит):")
    cursor.execute("SELECT fio_patient, diagnosis FROM Пациент WHERE diagnosis LIKE '%гастрит%' OR diagnosis LIKE '%бронхит%'")
    for row in cursor.fetchall():
        print(f" - {row[0]} (Диагноз: {row[1]})")

    print("\n 3. Пациенты, лечащиеся у конкретных специалистов (Петров или Волков):")
    cursor.execute("SELECT fio_patient, fio_doctor FROM Пациент WHERE fio_doctor LIKE '%Петров%' OR fio_doctor LIKE '%Волков%'")
    for row in cursor.fetchall():
        print(f" - {row[0]} (Врач: {row[1]})")

    cursor.execute("UPDATE Пациент SET cost = 25000.00 WHERE diagnosis = 'Пневмония'")
    cursor.execute("UPDATE Пациент SET diagnosis = 'ОРВИ (осложнение)' WHERE fio_patient LIKE '%Иванов%'")
    cursor.execute("UPDATE Пациент SET fio_doctor = 'Зав. отделением Смирнов А.А.' WHERE fio_patient LIKE '%Федоров%'")

    print_table("Таблица после проведения 3-х операций редактирования")

    cursor.execute("DELETE FROM Пациент WHERE fio_patient LIKE '%Григорьев%'")
    cursor.execute("DELETE FROM Пациент WHERE id = 8")
    cursor.execute("DELETE FROM Пациент WHERE cost <= 5000.00")

    print_table("Итоговая таблица после проведения 3-х операций удаления")