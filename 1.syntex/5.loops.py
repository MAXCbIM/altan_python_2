# *** Циклы (операторы циклов) ***

# Оператор while

#  бесконечный цикл (условия всегда истинно "True")
# while True:
#     print("Hello!")

# Цикл (while) прерывающийся по условии
num = 0

# while num < 10:
#     # print(num)
#     # инкремент
#     # num = num + 1 # длинная запись
#     num += 1 # короткая запись (делает ту же работу)
#     print(num)

#  Прерывание цикла по дополнительному условию
num = 10

# while num > 0:
#     print(num)
#     if num == 5:
#         # инструкция прерывания цикла
#         break # остановка выключает все циклы
#     # декремент (уменьшение величины)
#     num -= 1

num = 80
# while num < 100:
#     s = input("Введите команду: ")
#     if s == "stop":
#         print("Bye bye!")
#         break
#     print(f"Вы ввели: {s}")
#     num += 10

# пропуск куска кода в теле цикла
# while True:
#     s = input("Введите слово ДА: ")
#     if s == "ДА":
#         print("Цикл продолжается! ")
#         continue
#     print("Циклу конец!")
#     break

# *** Оператор цикла (for) ***

# 1.Читает значение элемента итерируемого обьекта по порядку
# 2.Значение присваевается в свою переменную
# 3.Выполняет блок кода своего тела

# for n in [1,2,3,4,5]:
#     print(n)

# for m in (10,20,30,40):
#     print(m)

# for _ in (1,2,3,4):
#     print("Hello!")

# for char in "python":
#     print(char)

my_tuple = (100, 1, 20, 1000)

# for i in my_tuple:
#     res = i * 2 
#     print(res)

# for i in my_tuple[::-1]:
#     print(i)

# *** Класс Range(диапазон) ***

r = range(2, 10)
# print(r)

# for n in range(2, 10):
#     print(n)

# for n in range(10):
#     print(n)

# for n in range(10, 100, 10)[::-1]:
#     print(n)

# *** Генератор списка ***

# автоматический список в диапазоне
my_list = [num for num in range(50, 100, 10)]

my_list = [num + 100 for num in range(10)]

my_list = [num for num in range(10) if num % 2 == 0]

# print(my_list)