import json


class Solver(object):

    def __init__(self, matrix):
        self.count = 0
        self.matrix = matrix
        """Solutions es para el sudoku vacio"""
        self.solutions = []

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

        coor = [0, 0]
        if self.get_empty(coor) == [-1, -1]:
            return True

        for num in range(1, 10):
            if self.is_placeable(coor[0], coor[1], num):
                self.matrix[coor[0]][coor[1]] = num
                if self.solve():
                    return True
                else:
                    self.matrix[coor[0]][coor[1]] = 0
        self.__incrementCount()
        return False

    def get_matrix(self):
        return self.matrix

    def __incrementCount(self):
        self.count += 1

    def get_count(self):
        return self.count

    """--- CODIGO DE PRUEBA PARA EMPTY SUDOKU (FUNCIONA AL 90%, FALTA HACER QUE EL SUDOKU SE VAYA MODIFICANDO EL TAMAÑO, Y QUE IMPRIMA LOS TIEMPOS---"""

    def get_empty_aux(self, coor, auxMatrix):
        for row in range(9):
            for col in range(9):
                if auxMatrix[row][col] == 0:
                    coor[0] = row
                    coor[1] = col
                    return coor
        coor[0] = -1
        coor[1] = -1
        return coor

    def is_in_row_aux(self, n, row, auxMatrix):
        for col in range(9):
            if auxMatrix[row][col] == n:
                return True
        return False

    def is_in_col_aux(self, n, col, auxMatrix):
        for row in range(9):
            if auxMatrix[row][col] == n:
                return True
        return False

    def is_in_box_aux(self, start_row, start_col, n, auxMatrix):
        for row in range(3):
            for col in range(3):
                if auxMatrix[row + start_row][col + start_col] == n:
                    return True
        return False

    def is_placeable_aux(self, row, col, n, auxMatrix):
        return not self.is_in_row_aux(n, row, auxMatrix) \
               and not self.is_in_col_aux(n, col, auxMatrix) \
               and not self.is_in_box_aux(row - row % 3, col - col % 3, n, auxMatrix)

    def solveEmpty(self, n):
        coor = [0, 0]
        firstcoor = [0, 0]
        if self.get_empty_aux(coor, self.matrix) == [-1, -1] or len(self.solutions) == 10:
            return True

        for num in range(1, n + 1):
            if self.is_placeable_aux(coor[0], coor[1], num, self.matrix) and not len(self.solutions) == 10:
                self.matrix[coor[0]][coor[1]] = num
                if self.solveEmpty(n):
                    print(self.matrix)
                    self.solutions.append(self.matrix)
                    print(len(self.solutions))
                    if len(self.solutions) == 10:
                        # print(self.solutions)
                        break
                    else:
                        if coor == firstcoor:
                            self.matrix[coor[0]][coor[1]] = 0
                else:
                    self.matrix[coor[0]][coor[1]] = 0
        return False
