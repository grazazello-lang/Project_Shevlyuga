# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 1 – 9.
# С начала суток прошло N секунд (N — целое). Найти количество
# полных часов, прошедших с начала суток.

import tkinter as tk
from tkinter import messagebox

class HoursCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор времени")
        self.root.geometry("450x400")
        self.root.resizable(False, False)

        # Цвета
        self.green_header = "#008080"
        self.green_footer = "#008080"
        self.bg_color = "#e8e8e8"
        self.field_bg = "#ffffff"
        self.field_border = "#4a90d9"
        self.result_color = "#006400"  # Тёмно-зелёный для результата

        # Главный контейнер
        main_frame = tk.Frame(root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # ===== ЗАГОЛОВОК =====
        header_frame = tk.Frame(main_frame, bg=self.green_header, height=40)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        header_label = tk.Label(
            header_frame,
            text="Калькулятор времени",
            font=("Arial", 14, "bold"),
            fg="white",
            bg=self.green_header
        )
        header_label.pack(pady=8)

        # ===== ОПИСАНИЕ ЗАДАЧИ =====
        desc_frame = tk.Frame(main_frame, bg=self.bg_color)
        desc_frame.pack(fill=tk.X, padx=10, pady=(10, 5))

        desc_text = (
            "С начала суток прошло N секунд (N — целое).\n"
            "Найти количество полных часов, прошедших с начала суток."
        )
        desc_label = tk.Label(
            desc_frame,
            text=desc_text,
            font=("Arial", 10),
            bg=self.bg_color,
            justify=tk.LEFT,
            anchor="w"
        )
        desc_label.pack(fill=tk.X)

        # ===== РАЗДЕЛИТЕЛЬ =====
        separator1 = tk.Frame(main_frame, bg="#cccccc", height=1)
        separator1.pack(fill=tk.X, padx=10, pady=5)

        # ===== ПОЛЕ ВВОДА =====
        input_frame = tk.Frame(main_frame, bg=self.bg_color)
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        input_label = tk.Label(
            input_frame,
            text="Введите количество секунд (N):",
            font=("Arial", 11),
            bg=self.bg_color,
            anchor="w"
        )
        input_label.pack(fill=tk.X, pady=(0, 5))

        self.seconds_entry = tk.Entry(
            input_frame,
            width=30,
            bg=self.field_bg,
            highlightbackground=self.field_border,
            highlightthickness=1,
            font=("Arial", 12),
            justify=tk.CENTER
        )
        self.seconds_entry.pack(pady=5)
        self.seconds_entry.focus()

        # ===== КНОПКА ВЫЧИСЛИТЬ =====
        btn_frame = tk.Frame(main_frame, bg=self.bg_color)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)

        self.calc_btn = tk.Button(
            btn_frame,
            text="Вычислить",
            font=("Arial", 11, "bold"),
            bg="#d0d0d0",
            activebackground="#b0b0b0",
            width=20,
            command=self.calculate
        )
        self.calc_btn.pack(pady=5)

        # ===== РАЗДЕЛИТЕЛЬ =====
        separator2 = tk.Frame(main_frame, bg="#cccccc", height=1)
        separator2.pack(fill=tk.X, padx=10, pady=5)

        # ===== БЛОК РЕЗУЛЬТАТА =====
        result_frame = tk.Frame(main_frame, bg=self.bg_color)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        result_title = tk.Label(
            result_frame,
            text="Результат вычисления:",
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            anchor="w"
        )
        result_title.pack(fill=tk.X, pady=(0, 10))

        # Контейнер для результатов
        results_container = tk.Frame(result_frame, bg=self.bg_color)
        results_container.pack(fill=tk.BOTH, expand=True)

        # Полные часы (главный результат)
        hours_frame = tk.Frame(results_container, bg=self.bg_color)
        hours_frame.pack(fill=tk.X, pady=5)

        tk.Label(
            hours_frame,
            text="Полных часов:",
            font=("Arial", 11),
            bg=self.bg_color,
            width=20,
            anchor="w"
        ).pack(side=tk.LEFT)

        self.hours_label = tk.Label(
            hours_frame,
            text="—",
            font=("Arial", 14, "bold"),
            fg=self.result_color,
            bg=self.field_bg,
            width=10,
            relief=tk.SUNKEN,
            padx=5
        )
        self.hours_label.pack(side=tk.LEFT, padx=5)

        # Минуты
        minutes_frame = tk.Frame(results_container, bg=self.bg_color)
        minutes_frame.pack(fill=tk.X, pady=5)

        tk.Label(
            minutes_frame,
            text="Остаток минут:",
            font=("Arial", 11),
            bg=self.bg_color,
            width=20,
            anchor="w"
        ).pack(side=tk.LEFT)

        self.minutes_label = tk.Label(
            minutes_frame,
            text="—",
            font=("Arial", 12),
            fg="#000080",
            bg=self.field_bg,
            width=10,
            relief=tk.SUNKEN,
            padx=5
        )
        self.minutes_label.pack(side=tk.LEFT, padx=5)

        # Секунды
        seconds_frame = tk.Frame(results_container, bg=self.bg_color)
        seconds_frame.pack(fill=tk.X, pady=5)

        tk.Label(
            seconds_frame,
            text="Остаток секунд:",
            font=("Arial", 11),
            bg=self.bg_color,
            width=20,
            anchor="w"
        ).pack(side=tk.LEFT)

        self.seconds_label = tk.Label(
            seconds_frame,
            text="—",
            font=("Arial", 12),
            fg="#800000",
            bg=self.field_bg,
            width=10,
            relief=tk.SUNKEN,
            padx=5
        )
        self.seconds_label.pack(side=tk.LEFT, padx=5)

        # Итоговое время
        total_frame = tk.Frame(results_container, bg=self.bg_color)
        total_frame.pack(fill=tk.X, pady=(15, 5))

        tk.Label(
            total_frame,
            text="Итого прошло:",
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            width=20,
            anchor="w"
        ).pack(side=tk.LEFT)

        self.total_label = tk.Label(
            total_frame,
            text="—",
            font=("Arial", 12, "bold"),
            fg=self.result_color,
            bg="#ffffcc",
            width=20,
            relief=tk.SUNKEN,
            padx=5
        )
        self.total_label.pack(side=tk.LEFT, padx=5)

        # ===== ФУТЕР =====
        footer_frame = tk.Frame(main_frame, bg=self.green_footer, height=35)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)

        footer_label = tk.Label(
            footer_frame,
            text="Формула: Часы = N // 3600, Минуты = (N % 3600) // 60, Секунды = N % 60",
            font=("Arial", 9),
            fg="white",
            bg=self.green_footer
        )
        footer_label.pack(pady=8)

        # Привязка клавиши Enter
        self.root.bind('<Return>', lambda event: self.calculate())

    def calculate(self):
        # Получаем значение из поля ввода
        input_value = self.seconds_entry.get().strip()

        # Валидация
        if not input_value:
            messagebox.showwarning("Ошибка", "Введите количество секунд!")
            return

        try:
            n = int(input_value)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число!")
            return

        if n < 0:
            messagebox.showerror("Ошибка", "Количество секунд не может быть отрицательным!")
            return

        # Вычисление
        full_hours = n // 3600
        remaining_minutes = (n % 3600) // 60
        remaining_seconds = n % 60

        # Вывод результата прямо в интерфейс
        self.hours_label.config(text=str(full_hours))
        self.minutes_label.config(text=str(remaining_minutes))
        self.seconds_label.config(text=str(remaining_seconds))
        self.total_label.config(
            text=f"{full_hours} ч {remaining_minutes} мин {remaining_seconds} сек"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = HoursCalculator(root)
    root.mainloop()