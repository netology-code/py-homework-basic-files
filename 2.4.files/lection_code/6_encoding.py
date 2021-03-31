# Пример 1 - Записываем файл в кодировке utf-8 (linux)
# with open('utf.txt', 'w', encoding='utf-8') as f:
#     f.write('Привет, мир!')

# Пример 2 - Записываем файл в кодировке cp1251 (windows)
# with open('cp.txt', 'w', encoding='cp1251') as f:
#     f.write('Привет, мир!')

# Пример 3 - Читаем файлы в байтах чтобы показать разницу в кодировках
# with open('cp.txt', 'rb') as f:
#     print("cp1251 ==> ", f.read())
# with open('utf.txt', 'rb') as f:
#     print("utf-8 ==> ", f.read())

# Пример 4 - Чтение файла с указанием неверной кодировки
# with open('cp.txt', 'r') as f:
#     print(f.read())

# Пример 5 - Чтение файла с указанием верной кодировки
# with open('cp.txt', 'r', encoding='cp1251') as f:
#     print(f.read())
