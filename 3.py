my_list = [x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0]
print(my_list)

print(sorted(list(range(20, 240, 20)) + list(range(21, 240, 21))))
