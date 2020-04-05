def two_max_sum(int_dict):
    if len(int_dict) == 3:
        return sum(int_dict) - min(int_dict)
    else:
        return f"Error! should be 3 parametrs, but {len(int_dict)} is given"


try:
    my_dict = input("Введите три числа через пробел ").split(" ")
    int_dict = list(map(int, my_dict))
    print(two_max_sum(int_dict))
except ValueError as e:
    print("ValueError!", e)
