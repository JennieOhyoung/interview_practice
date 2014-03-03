#1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.


class Matrix(object):

    def __init__(self,matrix):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.matrix = matrix

    def __str__(self):
        row = ""
        for i in self.matrix:
            row = row + "["
            for j in i:
                row = row + " " + str(j) + " "
            row = row + "]\n"
        return row

    def zero_col_row(self):
        col_zero = []
        row_zero = []
        for i, row in enumerate(self.matrix):
            for j, val in enumerate(row):
                if val == 0:
                    col_zero.append(j)
                    row_zero.append(i)
        for i in row_zero:
            self.row_turn(i)
        for j in col_zero:
            self.col_turn(j)

    def row_turn(self, i):
        new_row = []
        for x in range(0, self.m):
            new_row.append(0)
        self.matrix[i] = new_row

    def col_turn(self,j):
        for y in self.matrix:
            y[j] = 0

matrix2 = Matrix([[1,2,3], [4,0,6], [7,8,9]])
# print str(matrix2)
# matrix2.zero_col_row()
# print str(matrix2)
