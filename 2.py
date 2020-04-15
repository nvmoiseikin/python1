class Road:

    def __init__(self, width, length):
        self._width = width
        self._length = length
        self._mass = 0.025
        self._thin = 5

    def calc(self):
        return self._length * self._width * self._mass * self._thin

    def print_calc(self):
        print(f"Для дороги длинной {self._length}м и шириной {self._width}м необходимо {self.calc():.0f}т асфальта")


rd = Road(width=20, length=5000)
rd.print_calc()
