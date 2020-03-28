try:
    arr = []
    ans = 0
    ch = input("Введите положительное число ")
    if int(ch) < 0:
        raise ValueError("отрицательное число")
    arr.append(ch)
    arr.append(arr[-1] + ch)
    arr.append(arr[-1] + ch)
    for el in arr:
      ans += int(el)
    print(f"Ваше число {ch}, а ответ {ans}")
except ValueError as e:
    print(f'Некоректные данные, ошибка "{e}"')