sep = input("Введите разделитель элементов ")
if bool(sep):
    my_list = input("Введите элементы через разделитель ").split(sep)
    ans = my_list[::2]
    for i, value in enumerate(my_list[1::2]):
        ans.insert(i*2, value)
    print("Ваш список:", my_list)
    print("Измененный список:", ans)
else:
    print("Разделитель нулевой, ошибка!")
