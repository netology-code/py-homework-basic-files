# Пример 1 - деление на ноль

try:
    100 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя")


# Пример 2 - try/except/else/finally

def get_index():
    data = []
    print(data[0])


def get_int():
    data = "word"
    print(int(data))


try:
    # get_index()
    # get_int()
    print("Начало работы")
except IndexError:
    print("Index Error")
except TypeError:
    print("type Error")
else:
    # Отработает если у нас нет исключений
    print("Все прошло успешно исключений нет")
    ...
finally:
    # выполнит код при выходе
    print("всегда выполнится")
    ...
