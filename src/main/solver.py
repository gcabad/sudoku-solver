class Solver(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def get_empty(self, coor):
        for row in range(9):
            for col in range(9):
                if self.matrix[row][col] == 0:
                    coor[0] = row
                    coor[1] = col
                    return coor
        coor[0] = -1
        coor[1] = -1
        return coor

    def is_in_row(self, n, row):
        for col in range(9):
            if self.matrix[row][col] == n:
                return True
        return False

    def is_in_col(self, n, col):
        for row in range(9):
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
               and not self.is_in_box(row - row % 3, col - col % 3, n)

    def solve(self):
        # TODO: fix backtracking

        l = [0, 0]
        if self.get_empty(l) == [-1, -1]:
            return True
        row = l[0]
        col = l[1]

        for num in range(1, 10):
            if self.is_placeable(row, col, num):
                # make tentative assignment
                self.matrix[row][col] = num

                # return, if success, ya!
                if self.solve():
                    return True

                # failure, unmake & try again
                self.matrix[row][col] = 0

        # this triggers backtracking
        return False
