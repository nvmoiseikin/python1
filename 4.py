my_list = [1, 2, 3, 1, 2, 4, 5, 9, 7, 1, 2, 5]

new_list = [my_list[x] for x in range(len(my_list)) if not(my_list[x] in my_list[:x] or my_list[x] in my_list[x+1:])]
print(my_list, new_list, sep="\n")