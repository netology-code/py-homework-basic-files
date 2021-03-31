# Шаг 1 - Открыть файл
file = open('data.txt')
print(type(file), "\n")

# Шаг 2 - Выполнить работу (пока читаем файл)
data = file.read()
print(data)
print(type(data), "\n")

# Шаг 3 - Закрыть файл
file.close()

# Проверим остались ли данные в памяти
print(f"То что у нас в памяти - {data}")

# data = file.read()
