import math


class Solver(object):

    def __init__(self, matrix):
        self.count = 0
        self.matrix = matrix
        """Solutions es para el sudoku vacio"""
        self.solutions = []

    def get_empty(self, coor):
        for row in range(len(self.get_matrix())):
            for col in range(len(self.get_matrix())):
                if self.matrix[row][col] == 0:
                    coor[0] = row
                    coor[1] = col
                    return coor
        coor[0] = -1
        coor[1] = -1
        return coor

    def is_in_row(self, n, row):
        for col in range(len(self.get_matrix())):
            if self.matrix[row][col] == n:
                return True
        return False

    def is_in_col(self, n, col):
        for row in range(len(self.get_matrix())):
            if self.matrix[row][col] == n:
                return True
        return False

    def is_in_box(self, start_row, start_col, n):
        for row in range(int(math.sqrt(len(self.get_matrix())))):
            for col in range(int(math.sqrt(len(self.get_matrix())))):
                if self.matrix[row + start_row][col + start_col] == n:
                    return True
        return False

    def is_placeable(self, row, col, n):
        return not self.is_in_row(n, row) \
               and not self.is_in_col(n, col) \
               and not self.is_in_box(row - row % int(math.sqrt(len(self.get_matrix()))),
                                      col - col % int(math.sqrt(len(self.get_matrix()))), n)

    def solve(self):
        coor = [0, 0]
        if self.get_empty(coor) == [-1, -1]:
            return True

        for num in range(1, len(self.get_matrix()) + 1):
            if self.is_placeable(coor[0], coor[1], num):
                self.matrix[coor[0]][coor[1]] = num
                if self.solve():
                    return True
                else:
                    self.matrix[coor[0]][coor[1]] = 0
        self.__incrementCount()
        return False

    def solve_empty(self):
        coor = [0, 0]
        if self.get_empty(coor) == [-1, -1]:
            return True
        for num in range(1, len(self.get_matrix()) + 1):
            if len(self.solutions) >= 10:
                break
            if self.is_placeable(coor[0], coor[1], num):
                self.matrix[coor[0]][coor[1]] = num
                if self.solve_empty():
                    solution = []
                    for x in self.matrix:
                        row = x[:]
                        solution.append(row)
                    self.solutions.append(solution)
                    self.matrix[coor[0]][coor[1]] = 0
                else:
                    self.matrix[coor[0]][coor[1]] = 0
        return False

    def get_matrix(self):
        return self.matrix

    def __incrementCount(self):
        self.count += 1

    def get_count(self):
        return self.count
