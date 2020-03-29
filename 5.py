def my_input(text):
    try:
        x = int(input(text))
        if x < 0:
            raise ValueError("отрицательное число")
        return x
    except ValueError as e:
        print(f'Некоректные данные, ошибка "{e}"')


s = my_input("Введите прибыль в рублях ")
z = my_input("Введите издержки в рублях ")
if s > z:
    print(f"Рентабельность фирмы {(s-z)/s:.2f}")
    n = my_input("Введите количество сотрудников ")
    print(f"Прибыль на одного сотрудника составляет {(s-z)/n:.2f} рублей")
else:
    print("Фирма убыточная!")
