my_list = [1, 2, 4, -1, 8, 9, 0, 2, 4, 3, -7]

new_list = [my_list[index] for index in range(len(my_list)) if index == 0 or my_list[index] > my_list[index-1]]
print(new_list)
