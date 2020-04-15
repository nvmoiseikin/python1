class Car:

    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.test()

    def go(self):
        print("Начинаем движение" if self._speed == 0 else f"Вы уже едите со скоростью {self._speed}")

    def stop(self):
        print("Делаем остоановку" if self._speed != 0 else f"Вы уже стоите")

    def turn(self, direction):
        print(f"Поворачиваем {direction}")

    def show_speed(self):
        print(f"Ваша скорость {self._speed} км/ч")

    def test(self):
        print(f"Машина с характеристиками: speed={self._speed}, color={self.color}, name={self.name}, is_police={self.is_police}")
        self.go()
        self.stop()
        self.show_speed()
        self.turn("влево")


class WorkCar(Car):

    def show_speed(self):
        print(f"Вы нарушаете скоростной режим, ваша скорость {self._speed} км/ч" if self._speed > 40 else f"Ваша скорость {self._speed} км/ч")


class TownCar(Car):

    def show_speed(self):
        print(f"Вы нарушаете скоростной режим, ваша скорость {self._speed} км/ч" if self._speed > 60 else f"Ваша скорость {self._speed} км/ч")


class PoliceCar(TownCar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f"Добро пожаловать в полицейскую машину" if self.is_police else f"Ошибка! Это поицейская машина")
        super().test()

    def test(self):
        pass


car = Car(speed=120, color="red", name="Копейка", is_police="false")
tcar = TownCar(speed=120,  color="red", name="Копейка", is_police="false")
pcar = PoliceCar(speed=0, color="red", name="Копейка", is_police="false")