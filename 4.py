try:
    max = 0
    ch = int(input("Введите положительное число "))
    if ch < 0:
        raise ValueError("отрицательное число")
    while ch > 0:
        dig = ch % 10
        #print(dig)
        max = dig if max < dig else max
        ch //= 10
    print(f"Самая большая цифра {max}")
except ValueError as e:
    print(f'Некоректные данные, ошибка "{e}"')