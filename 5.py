my_list = [1, 92, 39, 45567, 5, 6, 123, 546, 21]

with open("5.txt", mode="wt+", encoding="utf-8") as file:
    file.write(" ".join(map(str, my_list)))
    file.seek(0)
    my_sum = sum(map(int, file.read().split(" ")))
    print(my_sum)
