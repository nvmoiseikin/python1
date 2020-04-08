from functools import reduce

my_list = range(100, 1000, 2)
print(my_list)
my_mull = reduce(lambda x, y: x * y, my_list)
print(my_mull, f"Знаков {len(str(my_mull))}, а примено 2,5 * 450 = {2.5 * 450}", sep="\n")