import json
import random


class Solver(object):

    def __init__(self, matrix):
        self.count = 0
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

        coor = [0, 0]
        if self.get_empty(coor) == [-1, -1]:
            return True

        for num in range(1, 10):
            if self.is_placeable(coor[0], coor[1], num):
                self.matrix[coor[0]][coor[1]] = num
                self.__incrementCount()
                # json.dump(self.matrix, open("../../resources/test/" + str(self.increment()) + ".json", "w+"))
                if self.solve():
                    return True
                else:
                    self.matrix[coor[0]][coor[1]] = 0
        return False

    def solveEmpty(self):
        # TODO: fix method. La clave esta en la parte de is_PLaceable!
        """  Como debería funcionar esto:
        #  1) Find all legal values of a given cell
        #  2) For each legal value, Go recursively and try to solve the grid
        Creo que el error está en que el programa funciona con una matriz interna que tiene como atributo de la clase. Deberíamos hacer que los metodos
        que chequean (get_empty, is_in_row, is_in_col, is_in_box, is_placeable) reciban como parametro una matriz, y no trabajar con la interna (self.matrix).
        Creo que la clave está en que al ejectuar el for y el is_placeable, cree una nueva matriz con ese valor o algo asi, para que cuando vuelva para atras haga otra matriz distinta o algo asi.
        estoy cansado, voy a dormir, mañana la sigo jaja. De ultima esto de acá no le des pelota que despues lo sigo.
        si lees este comentario hasta el final te mereces un buen nepe."""

        x = 0
        while x < 10:
            coor = [0, 0]
            if self.get_empty(coor) == [-1, -1]:
                return True

            for num in range(1, 10):
                if self.is_placeable(coor[0], coor[1], num):
                    self.matrix[coor[0]][coor[1]] = num
                    if self.solve():
                        x+=1
                        print(self.get_matrix())
                    else:
                        self.matrix[coor[0]][coor[1]] = 0
                return False

    def get_matrix(self):
        return self.matrix

    def __incrementCount(self):
        self.count += 1

    def get_count(self):
        return self.count
