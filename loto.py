import random
from functools import reduce


class Player:
    """"""

    def __init__(self, name, is_computer):
        self.name = name
        self.is_computer = is_computer
        self.card = self.gen_card()

    def gen_card(self, num_range=90, line_len=9, height=3, deleted_in_line=4):  # Создает карточку игрока
        nums = list(range(1, num_range + 1))
        random.shuffle(nums)
        card_nums = [(sorted(nums[line_id:line_id + line_len]), self.rand_choices(deleted_in_line, line_len)) for
                     line_id in range(0, line_len * height, line_len)]
        card_nums = [[num if ind not in deleted else None for ind, num in enumerate(line)] for line, deleted in
                     card_nums]
        card_nums = reduce(lambda x, y: x + y, card_nums)
        card_nums = dict(
            [(num, num) if num is not None else ("none_" + str(ind), "  ") for ind, num in enumerate(card_nums)])
        return card_nums

    def rand_choices(self, choices, length):
        line_deleted = list(range(0, length))
        random.shuffle(line_deleted)
        return line_deleted[:choices]

    def turn(self, num, ans):  # Проверяет ответ человека
        if ans != "y" and ans != "n":
            return "lose"
        if num in self.card.values() and ans == "y":
            return self.mark(num)
        elif num in self.card.values() and ans == "n" or num not in self.card.values() and ans == "y":
            return "lose"
        return "next"

    def mark(self, num):  # Зачеркиваем бочонок
        if num in self.card.values():
            self.card[num] = "--"
        if not bool([item for item in self.card.values() if item != "  " and item != "--"]):
            return "win"
        return "next"

    def __str__(self, line_len=9, height=3):  # Выводит карточку игрока в консоль
        card = list(map(lambda x: str(x) + " " if x != "  " and x != "--" and x < 10 else str(x), self.card.values()))
        name = self.name if len(self.name) < (line_len * 3 - 4) else self.name[:line_len * 3 - 4]
        player_border = "-" * ((line_len * 3 - len(name)) // 2 - 1)
        player = player_border + " " + name + " " + player_border + "-" * ((len(name) - 1) % 2) + "\n"
        border = "---" * line_len
        return player + "\n".join([" ".join(card[line_id:line_id + line_len]) for line_id in
                                   range(0, height * line_len, line_len)]) + "\n" + border


class Game:
    """"""

    def __init__(self, *players, num_range=90):
        self.players = list(players)
        self.num_range = num_range
        self.nums = list(range(1, num_range + 1))
        random.shuffle(self.nums)
        self.winner = []

    def start(self):
        for round, num in enumerate(self.nums, start=1):
            print(f"Новый бочонок: {num} (осталось {self.num_range - round})")
            for id, player in enumerate(self.players[:]):
                if not player.is_computer:
                    print(player)
                turn = player.turn(num, input("Зачеркнуть цифру? (y/n) ")) if not player.is_computer else player.mark(
                    num)
                if player.is_computer:
                    print(player)
                if turn == "lose":
                    self.players.pop(id)  # Удаляем проигравшего игрока
                    print(f"Нас покидает {player.name}")
                elif turn == "win":  # Если кто-то собрал карточку
                    self.winner.append(player.name)
            if len(self.players) == 0:  # Люди одновременно ошиблись и нет победителя
                self.winner.append("нет победителя")
                break
            elif len(self.players) == 1:  # Люди ошиблись и остался один победитель
                self.winner.append(self.players[0].name)
                break
            if len(self.winner) > 0:  # Если кто-то собрал карточку
                break
        return self

    def __str__(self):
        return f"Победил(и) {' ,'.join(self.winner)}"


comp1 = Player(name="computer1 smart smart smart", is_computer=1)
comp2 = Player(name="computer2", is_computer=1)
human = Player(name="Ivan", is_computer=0)
# print(comp1, human, sep="")
winner = Game(comp1, human, comp2).start()
print(winner)
