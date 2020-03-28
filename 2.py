try:
    ch = int(input("Введите число в секундах "))
    if ch < 0:
        raise ValueError("отрицательное число")
    seconds = ch % 60
    minutes = ch % 3600 // 60
    hours = ch // 3600
    print(f"{hours}:{minutes}:{seconds}")
except ValueError as e:
    print(f'Некоректные данные, ошибка "{e}"')