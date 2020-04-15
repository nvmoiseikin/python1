import time
from threading import Thread
from itertools import cycle

class TrafficLight(Thread):

    def __init__(self, num):
        self.time = my_start
        self.__num = "traffic_light_" + str(num)
        super().__init__(name=self.__num, daemon=True)
        self.__color = None
        self.__data = {1: {"color": "красный", "time": 7},
                       2: {"color": "желтый", "time": 2},
                       3: {"color": "зеленый", "time": 7}}
        self.__iter = cycle(self.__data)

    def run(self):
        self.__change_color()
        while self.__color is not None:
            self.__change_color()

    def get_color_data(self):
        return self.__data.get(next(self.__iter))

    def __change_color(self):
        color_data = self.get_color_data()
        print(color_data.get("color"), "<<<Время с начачала программы {:.0f}>>>".format(time.time() - self.time), self.__num)
        self.__color = color_data.get("color")
        time.sleep(color_data.get("time"))

    def stop(self):
        self.__color = None
        self.__iter = cycle(self.__data)


#Захотел, чтобы можно было создавать независимые светофоры(обЪекты класса) и чтобы их можно было останавливать.
#Насколько это криво??? Не нашел как убивать?
my_start = time.time()
tf1 = TrafficLight(1)
tf1.start()
time.sleep(1)
print("sleep 1", "<<<Время с начачала программы {:.0f}>>>".format(time.time() - my_start))
tf2 = TrafficLight(2)
tf2.start()
time.sleep(10)
print("sleep 10", "<<<Время с начачала программы {:.0f}>>>".format(time.time() - my_start))
tf1.stop()
time.sleep(10)
print("sleep 10", "<<<Время с начачала программы {:.0f}>>>".format(time.time() - my_start))
tf1.run()

