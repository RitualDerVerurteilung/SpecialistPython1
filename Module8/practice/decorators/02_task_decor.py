# Напишите функцию декоратор, которая округляет значение декорируемой функции до двух знаков после  запятой.
# Если округление невозможно, например там строка, или не требуется(целое число) то оставляем результат без изменений.
# Примечание: используйте встроенную функцию round()
def decor(func):
    def wrapper(*args, **kwargs):
        try:
            print(round(func(*args, **kwargs), 2))
        except TypeError:
            print(func(*args, **kwargs))
    return wrapper


@decor
def privet(x):
    return x


privet(123.456)
