n = 0
f = True
input_dict = {"название":  "Введите название {n}-ого товара (для завершения ввода товаров введите '*') ",
 "цена":  "Введите цену {n}-ого товара ",
 "колиество":  "Введите количество {n}-ого товара ",
 "ед":  "Введите единицы измерения {n}-ого товара "}
struct1 = []
struct2 = {}


while f == True:
    n += 1
    struct1.append((n, {}))
    for name, text in input_dict.items():
        value = input(text.replace("{n}", str(n)))[:20]
        if value == "*":
            f = False
            print("Конец ввода!")
            break
        struct1[-1][1][name] = value
        if n == 1:
            struct2[name] = set()
        struct2[name].add(value)


struct1.pop()
print(struct1)
print(struct2)