# Пример 1 - попытка записать в файл который открыт только на чтение
with open('data_3.txt') as f:
    f.write('Привет, мир!')

# Пример 2 - попытка записать в файл который открыт на запись
# with open('data_3.txt', 'w') as f:
#     f.write('Привет, мир!')

# Пример 3 - попытка прочитать в файл который открыт на запись
# with open('data_3.txt', 'w') as f:
#     print(f.read())

# Пример 4 - попытка прочитать в файл который открыт на запись И чтение
# with open('data_3.txt', 'wr') as f:
#     # Ошибка
#     print(f.read())

# Пример 5 - попытка записать две строки но в разных сессиях в файл который открыт на запись
# with open('data_3.txt', 'w') as f:
#     f.write('Первая строка!')
# with open('data_3.txt', 'w') as f:
#     f.write('Вторая строка!')

#  Пример 6 - Дозапись файла
# with open('data_3.txt', 'a') as f:
#     f.write('Первая строка! \n')
# with open('data_3.txt', 'a') as f:
#     f.write('Вторая строка! \n')

# Пример 5 - Битовое чтение
# with open('data_3.txt', 'rb') as f:
#     data = f.read()
#     print(type(data))
#     print(data)


# Пример 6 - Битовая чтение строки
# with open('data_3.txt', 'rb') as f:
#     print(f.readline())
