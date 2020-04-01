a = "aa"
my_list = [1, "0", None, True, [2, False], (), set([2, 3, 3, 3, 2, 3]), b"10asw", f"затупил {a}", {"hello": "world"}]
for item in my_list:
    print(item, type(item), sep=": ")