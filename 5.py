def my_sum(int_dict, prev_sum=0):
    return sum(int_dict) + prev_sum


prev_sum = 0
while True:
    try:
        my_dict = input("Введите числа через пробел. (Для окончания введите *) ").split(" ")
        if my_dict == "*":
            break
        int_dict = list(map(int, my_dict))
        prev_sum = my_sum((int_dict), prev_sum)
        print("Текущая сумма:", prev_sum)
    except ValueError as e:
        print("ValueError!", e)
        break
print("end")
