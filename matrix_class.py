from typing import List, Any

class Matrix():
    def __init__(self, input_rows : List[List[Any]]):
        rows = len(input_rows)
        cols = len(input_rows[0])

        self.matrix : List[List[Any]] = input_rows
        self.cols : int = cols
        self.rows : int = rows
        self.cur_row : int = 0

        if not input_rows:
            return None
        for row in input_rows:
            if len(row) != rows or len(row) != cols:
                raise Exception("not same sizes")
            cols = len(row)

    # def __add__(self, another) -> Matrix:
    def __add__(self, another):
        if self.cols != another.cols:
            raise Exception("cols dimension not same")
        if self.rows != another.rows:
            raise Exception("rows dimension not same")
        answer = [[0]*self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                answer[i][j] = self.matrix[i][j] + another.matrix[i][j]
        
        return Matrix(answer)
    
    def __sub__(self, another):
        if self.cols != another.cols:
            raise Exception("cols dimension not same")
        if self.rows != another.rows:
            raise Exception("rows dimension not same")
        answer = [[0]*self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                answer[i][j] = self.matrix[i][j] - another.matrix[i][j]
        
        return Matrix(answer)
    
    def __mul__(self, another):
        if self.cols != another.rows:
            raise Exception("wrong dimension")
        answer = [[0]*another.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(another.cols):
                answer[i][j] = 0
                for k in range(self.cols):
                    answer[i][j] += self.matrix[i][k] * another[k][j]
        
        return Matrix(answer)

    def __getitem__(self, index):
        return self.matrix[index]
    
    def __eq__(self, another):
        if self.cols != another.cols:
            raise Exception("cols dimension not same")
        if self.rows != another.rows:
            raise Exception("rows dimension not same")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] != another.matrix[i][j]:
                    return False
        return True
    
    def __hash__(self):
        items = tuple(elem for row in self.matrix for elem in row)
        return hash(items)

    def __repr__(self):
        return (f"Matrix: {str(self.matrix)}")
    
    # def __iter__(self):
    #     for row in self.matrix:
    #         yield row
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur_row == self.rows:
            self.cur_row=0
            raise StopIteration
        row = self.matrix[self.cur_row]
        self.cur_row+=1
        return row


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

# Строковое представление
print(m1)  # [[1, 2], [3, 4]]
print(repr(m1))  # Matrix([[1, 2], [3, 4]])

# Сложение матриц
m3 = m1 + m2
print(m3)  # [[6, 8], [10, 12]]

# Вычитание матриц
m4 = m1 - m2
print(m4)  # [[-4, -4], [-4, -4]]

# Умножение матриц
m5 = m1 * m2
print(m5)  # [[19, 22], [43, 50]]

# Сравнение матриц
print(m1 == m2)  # False
print(m1 == Matrix([[1, 2], [3, 4]]))  # True

# Индексация
print(m1[0][1])  # 2

# Хэширование
matrix_set = {m1, m2}
print(m1 in matrix_set)  # True

for row in m5:
    print(row)


for row in m5:
    print(row)
    
for row in m5:
    print(row)