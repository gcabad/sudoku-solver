import csv
import os

from src.exception.input_exception import *
from src.main.menu import Menu
from src.main.solver import Solver
import json


def parse_csv_to_array(csv_file):
    # TODO: leer sudokus continuos, agregar manejo de errores si no cumplen la condicion 9x9, retornar lista de matrices
    try:
        reader = csv.reader(open(csv_file, "r"))
        matrix = []
        # Convierte el csv a un 2D array
        for line in reader:
            row = []
            for litem in line:
                row.append(int(litem))
            if len(row) != 9:
                raise InputException("El sudoku no es de tamaño 9")
            matrix.append(row)
        if len(matrix) != 9:
            raise InputException("El sudoku no es de tamaño 9")
        return matrix
    except FileNotFoundError as e:
        print(e)


def parse_array_to_csv(matrix, filename):
    writer = csv.writer(open(filename, "w+"), delimiter=",")
    for row in matrix:
        writer.writerow(row)


def solve():

    menu = Menu()
    try:
        filename = menu.show_options()
        path = "../../resources/" + filename + ".json"
        if os.path.exists(path):
            matrix = json.load(open(path, "r"))
            menu.show_savegame_found(filename)
        else:
            menu.show_savegame_not_found(filename)
            matrix = parse_csv_to_array("../../resources/sudokus.csv")
        solver = Solver(matrix)
        json.dump(solver.matrix, open(path, "w+"))
    except KeyboardInterrupt:
        menu.show_keyboard_interrupt(filename)
        json.dump(filename, open(path, "w+"))


if __name__ == '__main__':
    solve()
