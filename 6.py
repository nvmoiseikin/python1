import math


def my_input(text):
    try:
        x = float(input(text))
        if x < 0:
            raise ValueError("отрицательное число")
        return x
    except ValueError as e:
        print(f'Некоректные данные, ошибка "{e}"')
        return -1


def my_math(a, b):
    x = math.log(b/a, 1.1)
    return math.ceil(x) + 1


a = my_input("Введите начальное значение в км ")
b = my_input("Введите конечное значение в км ")
if a == -1 or b == -1:
    print("Ошибка в введенных данных!")
elif b >= a:
    print(f"Понадобится {my_math(a, b)} дней")
else:
    print("Ошибка, конечное значение должно быть больше")