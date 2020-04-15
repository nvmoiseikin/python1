class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {wage: wage, bonus: bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя - {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Полный доход - {sum(self._income.values())} рублей")


ya = Position(name="Nikita", surname="Moiseikin", position="front-end", wage=45000, bonus=10000)
ya.get_full_name()
ya.get_total_income()
