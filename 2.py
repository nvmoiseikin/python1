from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def __init__(self, size_param):
        pass

    @abstractmethod
    def __it__(self):
        pass


class Storage:
    def __init__(self):
        self.items = []

    def __add__(self, item):
        self.items.append(item)
        return self

    def __radd__(self, item):
        self.items.append(item)
        return self

    def __str__(self):
        return "Необходимо {} м".format(str(round(sum(map(lambda x: x.__it__, self.items)), 1)))


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def __it__(self):
        return round(self.size/6.5 + 0.5, 1)


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def __it__(self):
        return round(self.height * 2 + 0.3, 1)


storage = Storage()
cl1 = Coat(62)
cl2 = Suit(10)
cl3 = Suit(7)
print(cl1 + storage + cl1 + cl2 + cl3)