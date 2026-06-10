# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу
import tkinter as tk
from tkinter import filedialog, messagebox

class ApplicationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Форма заявки")
        self.root.geometry("520x520")
        self.root.resizable(False, False)

        # Цвета
        self.green_header = "#008080"
        self.green_footer = "#008080"
        self.bg_color = "#e8e8e8"
        self.field_bg = "#ffffff"
        self.field_border = "#4a90d9"
        self.red_asterisk = "#ff0000"

        # ===== ВАЖНО: инициализируем атрибуты =====
        self.name_entry = None
        self.email_entry = None
        self.subject_entry = None
        self.file_entries = []

        # Главный контейнер
        main_frame = tk.Frame(root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # ===== ЗАГОЛОВОК =====
        header_frame = tk.Frame(main_frame, bg=self.green_header, height=35)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        header_label = tk.Label(
            header_frame,
            text="Форма заявки",
            font=("Arial", 14, "bold"),
            fg="white",
            bg=self.green_header
        )
        header_label.pack(pady=6)

        # ===== ИНФОРМАЦИЯ О ВЛОЖЕНИЯХ =====
        info_frame = tk.Frame(main_frame, bg=self.bg_color)
        info_frame.pack(fill=tk.X, padx=5, pady=(5, 2))

        info_text = (
            "Допустимые типы вложений: zip, rar, txt, doc, jpg, png, gif, odt, xml\n"
            "Макс. размер каждого файла: 1024kb.\n"
            "Макс. общий размер файла: 2048kb."
        )
        info_label = tk.Label(
            info_frame,
            text=info_text,
            font=("Arial", 9),
            bg=self.bg_color,
            justify=tk.LEFT,
            anchor="w"
        )
        info_label.pack(fill=tk.X)

        # ===== РАЗДЕЛИТЕЛЬ =====
        separator1 = tk.Frame(main_frame, bg="#cccccc", height=1)
        separator1.pack(fill=tk.X, padx=5)

        # ===== ПОЛЯ ФОРМЫ =====
        fields_frame = tk.Frame(main_frame, bg=self.bg_color)
        fields_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        row = 0

        # Ваше имя
        self._create_labeled_entry(fields_frame, row, "Ваше имя:", required=True)
        row += 1

        # Ваш Email
        self._create_labeled_entry(fields_frame, row, "Ваш Email:", required=True)
        row += 1

        # Тема письма
        self._create_labeled_entry(fields_frame, row, "Тема письма:", required=False)
        row += 1

        # Прикрепить файл 1
        self._create_file_field(fields_frame, row)
        row += 1

        # Прикрепить файл 2
        self._create_file_field(fields_frame, row)
        row += 1

        # Прикрепить файл 3
        self._create_file_field(fields_frame, row)
        row += 1

        # Ваше сообщение
        msg_label = tk.Label(
            fields_frame,
            text="Ваше сообщение:",
            font=("Arial", 10),
            bg=self.bg_color,
            anchor="w"
        )
        msg_label.grid(row=row, column=0, sticky="w", pady=(5, 0))

        asterisk_msg = tk.Label(
            fields_frame,
            text="*",
            font=("Arial", 10, "bold"),
            fg=self.red_asterisk,
            bg=self.bg_color
        )
        asterisk_msg.grid(row=row, column=1, sticky="w", pady=(5, 0))

        row += 1

        self.message_text = tk.Text(
            fields_frame,
            height=8,
            width=50,
            bg=self.field_bg,
            highlightbackground=self.field_border,
            highlightthickness=1,
            font=("Arial", 10),
            wrap=tk.WORD
        )
        self.message_text.grid(row=row, column=0, columnspan=3, sticky="ew", pady=(2, 5))

        fields_frame.columnconfigure(2, weight=1)

        # ===== РАЗДЕЛИТЕЛЬ =====
        separator2 = tk.Frame(main_frame, bg="#cccccc", height=1)
        separator2.pack(fill=tk.X, padx=5)

        # ===== ФУТЕР С КНОПКАМИ =====
        footer_frame = tk.Frame(main_frame, bg=self.green_footer, height=45)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)

        btn_frame = tk.Frame(footer_frame, bg=self.green_footer)
        btn_frame.pack(expand=True)

        self.send_btn = tk.Button(
            btn_frame,
            text="Отправить Email",
            font=("Arial", 10),
            bg="#d0d0d0",
            activebackground="#b0b0b0",
            width=18,
            command=self.send_email
        )
        self.send_btn.pack(side=tk.LEFT, padx=10, pady=5)

        self.clear_btn = tk.Button(
            btn_frame,
            text="Отчистить",
            font=("Arial", 10),
            bg="#d0d0d0",
            activebackground="#b0b0b0",
            width=14,
            command=self.clear_form
        )
        self.clear_btn.pack(side=tk.LEFT, padx=10, pady=5)

    def _create_labeled_entry(self, parent, row, label_text, required=False):
        label = tk.Label(
            parent,
            text=label_text,
            font=("Arial", 10),
            bg=self.bg_color,
            anchor="w",
            width=18
        )
        label.grid(row=row, column=0, sticky="w", pady=3)

        entry = tk.Entry(
            parent,
            width=35,
            bg=self.field_bg,
            highlightbackground=self.field_border,
            highlightthickness=1,
            font=("Arial", 10)
        )
        entry.grid(row=row, column=1, sticky="ew", pady=3)

        if required:
            asterisk = tk.Label(
                parent,
                text="*",
                font=("Arial", 10, "bold"),
                fg=self.red_asterisk,
                bg=self.bg_color
            )
            asterisk.grid(row=row, column=2, sticky="w", pady=3)

        parent.columnconfigure(1, weight=1)

        # ===== ВАЖНО: сохраняем ссылки на поля =====
        if "Ваше имя" in label_text:
            self.name_entry = entry
        elif "Ваш Email" in label_text:
            self.email_entry = entry
        elif "Тема письма" in label_text:
            self.subject_entry = entry

    def _create_file_field(self, parent, row):
        label = tk.Label(
            parent,
            text="Прикрепить файл:",
            font=("Arial", 10),
            bg=self.bg_color,
            anchor="w",
            width=18
        )
        label.grid(row=row, column=0, sticky="w", pady=3)

        entry = tk.Entry(
            parent,
            width=30,
            bg=self.field_bg,
            highlightbackground=self.field_border,
            highlightthickness=1,
            font=("Arial", 10)
        )
        entry.grid(row=row, column=1, sticky="ew", pady=3)

        browse_btn = tk.Button(
            parent,
            text="Обзор...",
            font=("Arial", 9),
            bg="#d0d0d0",
            activebackground="#b0b0b0",
            command=lambda e=entry: self.browse_file(e)
        )
        browse_btn.grid(row=row, column=2, sticky="w", padx=(5, 0), pady=3)

        parent.columnconfigure(1, weight=1)

        # Сохраняем ссылку на поле файла
        self.file_entries.append(entry)

    def browse_file(self, entry):
        filetypes = [
            ("Все допустимые файлы", "*.zip *.rar *.txt *.doc *.jpg *.png *.gif *.odt *.xml"),
            ("ZIP файлы", "*.zip"),
            ("RAR файлы", "*.rar"),
            ("Текстовые файлы", "*.txt"),
            ("DOC файлы", "*.doc"),
            ("Изображения", "*.jpg *.png *.gif"),
            ("ODT файлы", "*.odt"),
            ("XML файлы", "*.xml"),
            ("Все файлы", "*.*")
        ]
        filepath = filedialog.askopenfilename(filetypes=filetypes)
        if filepath:
            entry.delete(0, tk.END)
            entry.insert(0, filepath)

    def send_email(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        subject = self.subject_entry.get().strip()
        message = self.message_text.get("1.0", tk.END).strip()

        errors = []
        if not name:
            errors.append("Ваше имя")
        if not email:
            errors.append("Ваш Email")
        if not message:
            errors.append("Ваше сообщение")

        if errors:
            messagebox.showwarning(
                "Ошибка",
                "Заполните обязательные поля:\n" + "\n".join(errors)
            )
        else:
            messagebox.showinfo("Успех", "Заявка успешно отправлена!")
            print(f"Имя: {name}")
            print(f"Email: {email}")
            print(f"Тема: {subject}")
            print(f"Сообщение: {message}")

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        for entry in self.file_entries:
            entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationForm(root)
    root.mainloop()