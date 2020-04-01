my_list = input("Введите элементы через пробел ").split(" ")
for i, value in enumerate(my_list, start=1):
    print(f"{i}: {value[:10]}")
