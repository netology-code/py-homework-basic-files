# Пример 1 - читаем файл целиком
with open('data_2.txt') as f:
    data = f.read()
    print(type(data))
    print(data)


# Пример 2 - читаем построчно
# with open('data_2.txt') as f:
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline() == '')
#     print(f.readline() is None)


# Пример 3 - читаем строки (все) - читается все,  но записывается в список
# with open('data_2.txt') as f:
#     lines = f.readlines()
#     print(type(lines))
#     print(len(lines))
#     print(lines[1])


# Пример 4 - читаем итеративно
# with open('data_2.txt') as file:
#     for line in file:
#         print(line.strip())
