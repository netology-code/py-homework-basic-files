import os
import time

# Пример 1 - получение пути от корня файловой системы к текущему каталогу
print("==> ", os.getcwd())

# Пример 2 - построение пути к файлу
file_path = os.path.join(os.getcwd(), 'data.txt.txt')
print("==> ", file_path)

# Пример 3 - Запись и чтение в файл без указания пути (относительный путь - т.к. относительно текущей директории)
with open('test.txt', 'w') as f:
    f.write(f'{time.time()}')
with open('test.txt', 'r') as f:
    print(f.read())

# Пример 4 - Запись и чтение в файл с указание пути (абсолютный путь)
file_path = os.path.join(os.getcwd(), 'test.txt')

with open(file_path, 'r') as f:
    print(f.read())
with open(file_path, 'r') as f:
    print(f.read())

# Пример 5 - Вложенный with
# пока менеджер контекста не закрыт, мы не может получить результат работы над файлом
with open('file.txt', 'w') as f:
    f.write('898-999-998-223')
    with open('file.txt') as f1:
        print(f1.read())

# with open('file.txt') as f1:
#     print(f1.read())
