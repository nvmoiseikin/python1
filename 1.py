class Matrix:

    def __init__(self, data):
        self.data = data
        self.h = len(data)
        self.w = len(data[0])

    def __str__(self):
        m_str = "\n"
        for line in self.data:
            m_str += " ".join(map(str, line)) + "\n"
        return m_str

    def __add__(self, other_matrix):
        if self.h == other_matrix.h and self.w == other_matrix.w:
            return Matrix(self._sum_data(other_matrix))
        else:
            return None

    def _sum_data(self, other_matrix):
        sum_data = []
        for line in range(0, self.h):
            sum_data.append([])
            for column in range(0, self.w):
                sum_data[line].append(self.data[line][column] + other_matrix.data[line][column])
        return sum_data

mx1 = Matrix([[1, 2], [3, 4]])
mx2 = Matrix([[3, 2], [5, 4]])
mx_mx = Matrix([[mx1, mx2], [2, mx1]])
print(mx1, mx2, mx1+mx2, mx_mx + mx_mx)
#Можно создавать матрицы матриц, только выводит плохо.