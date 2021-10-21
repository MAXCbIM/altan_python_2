# *** Генератор паролей ***

# password_salt(сайта "google")

# импортирование модулей
import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar

def generator():
    # чтение строки сырой пароли
    pwd_str = pwd.get()
    # кодирование в байт-строке
    byte_str = pwd_str.encode()
    # хеширование
    hash_str = hashlib.sha256(byte_str)
    # преобразование хеш-строки в обычную строку
    hex_str = hash_str.hexdigest()[:10]
    # вывод хеш-строки
    # print(hex_str)
    hash_pwd.set(hex_str)

# generator("qwerty")

# обьект окна
window = Tk()
window.title("PWD generator v.0.1")

# обьект для хранения строк
pwd = StringVar()
hash_pwd = StringVar()

# тестирование StringVar
# pwd.set("qwerty")
# print(pwd.get())

# виджет (компонент) текстовой метки
lbl = Label(text="Пароль:")
lbl.grid(row=0, column=0)

# виджет поля ввода
Entry(textvariable=pwd).grid(row=0, column=1)

# виджет кнопки
Button(text="СТАРТ", command=generator).grid(row=1, column=0)

# виджет поля вывода
Entry(textvariable=hash_pwd).grid(row=1, column=1)

# точка входа программы (место, где программа запускается)
window.mainloop()