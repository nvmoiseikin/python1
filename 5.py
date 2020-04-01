rait_list = [10, 9, 7, 5, 5, 5, 4, 2, 2, 2, 1, 1]


def rait_insert(list, new):
    start, end = (0, len(list))
    print(end)
    i = 0
    while start < end:
        mid = (start + end) // 2
        # print("mid", mid, "start", start, "end", end)
        if new > list[mid]:
            end = mid
        else:
            start = mid + 1
        i += 1
        if i > 100:
            break
    list.insert(start, [new])
    # для удобства новый рейтинг помещен в список []
    print(f"Новый список рейтингов: {list}, число итераций: {i}")


try:
    new_rait = int(input("Введите свой рейтинг "))
    if new_rait < 0:
        raise ValueError("рейтинг должен быть больше 0")
    rait_insert(rait_list, new_rait)
except ValueError as e:
    print(f"Неверные данные: {e}")