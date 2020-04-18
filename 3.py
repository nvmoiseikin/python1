class Cell:

    def __init__(self, size):
        self.size = int(size)
        if size <= 0:
            print(f"Error! Cell size should be positive, but {size} is given")
            self.size = 1

    def __add__(self, other_cell):
        return Cell(self.size + other_cell.size)

    def __sub__(self, other_cell):
        return Cell(self.size - other_cell.size)

    def __mul__(self, other_cell):
        return Cell(self.size * other_cell.size)

    def __truediv__(self, other_cell):
        return Cell(self.size // other_cell.size)

    def make_order(self, k):
        return ("*" * k + "\n") * (self.size // k) + "*" * (self.size % k)


cell1 = Cell(12)
cell2 = Cell(7)
cell3 = (cell1 - cell2) * cell2
cell4 = cell1 / (cell2 - cell1)
print(cell3.make_order(6))
