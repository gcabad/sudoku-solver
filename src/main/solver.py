class Solver(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def get_empty(self):
        for row in self.matrix:
            for col in row:
                if self.matrix[row][col] == 0:
                    return col, row
        return -1, -1

    def is_in_row(self, n, row):
        for col in self.matrix:
            if self.matrix[row][col] == n:
                return True
        return False

    def is_in_col(self, n, col):
        for row in self.matrix:
            if self.matrix[row][col] == n:
                return True
        return False

    def is_in_box(self, start_row, start_col, n):
        for row in range(3):
            for col in range(3):
                if self.matrix[row + start_row][col + start_col] == n:
                    return True
        return False

    def is_placeable(self, row, col, n):
        return not self.is_in_row(n, row) \
               and not self.is_in_col(n, col) \
               and not self.is_in_box(row - row % 3, col - col % 3, n) \
               and not self.matrix[row][col] == 0
