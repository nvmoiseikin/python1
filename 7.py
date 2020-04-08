def my_fact(n):
    res = 1
    for i in range(1, min(n + 1, 10)):
        res *= i
        yield res


for el in my_fact(20):
    print(el)
