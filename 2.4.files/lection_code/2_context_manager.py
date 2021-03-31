def is_closed(file_):
    """
    Функция принимает объект файл и проверяет его состояние
    """
    if file_.closed:
        print('Файл закрыт')
    else:
        print('Файл открыт')


# Эквивалентно
# f = open("data.txt") == with open("data.txt") as f


# Пример 1 - Открыть файл, прочитать закрыть
with open('data.txt') as f:
    print(type(f))
    data = f.read()
    is_closed(f)

is_closed(f)

# with open('data.txt') as f:
#     data = f.read()
#     is_closed(f)
#     1 / 0


# try:
#     with open('data.txt') as f:
#         data = f.read()
#         is_closed(f)
#         1 / 0
# except ZeroDivisionError:
#     is_closed(f)
