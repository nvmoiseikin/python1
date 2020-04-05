def my_pow(x, y):
    if y == 2:
        return x * x
    elif y == 0:
        return 1
    elif y < 0:
        return 1/my_pow(x, -y)
    elif y % 2 == 0:
        return my_pow(my_pow(x, y//2), 2)
    else:
        return my_pow(x, y-1) * x


print("2^-4", my_pow(2, -4))
print("2^-5", my_pow(2, -5))
print("2^7", my_pow(2, 7))
print("3^-1", my_pow(3, -1))
print("5^-21", my_pow(5, -21))
print("5^22", my_pow(5, 22))

