def my_div(a, b):
    if b == 0:
        return "Error! Division by zero"
    else:
        return a/b


try:
    a, b = input("Введите два числа через пробел ").split(" ")
    print(my_div(int(a), int(b)))
except ValueError as e:
    print("ValueError!", e)
