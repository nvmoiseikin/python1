name = "Ivanov Ivan Ivanovich"
first_name = name.split(" ")[0]
print(first_name)
year = "1995"
now = 2020
age = now - int(year)
print(age)
print(bool(year))
print(bool(age))
print(0, bool(0))
print("'0'", bool("0"))
print("''", bool(""))