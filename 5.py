class Stationery:

    def __init__(self, title):
        self._title = title

    def draw(self):
        return f"Запуск отрисовки {self._title}"


def generator_draw(name):
    def my_draw(self):
        return f"Запуск отрисовки {self._title} ({name})"
    return my_draw


types = ["Pen", "Pencil", "Handle"]
classes = {}
for name in types:
    classes[name] = type(name, (Stationery, ), {"draw": generator_draw(name)})
    # classes.__setitem__(name, type(name, (Stationery, ), {"draw": lambda self: "Запуск отрисовки " + name}))
    # ОЧЕНЬ ИНТЕРЕСНО, ЧТО ЕСЛИ ВМЕСТО ОБЫЧНОЙ generator_draw НАПИСАТЬ ЛЯМБДА ФУНКЦИЮ БУДЕТ РАБОТАТЬ НЕ КОРРЕКТНО???

pn = classes["Pen"](10101)
print(pn.draw())
pn2 = classes["Pencil"](20202)
print(pn2.draw())
