import csv

from .exception.exceptions import *
from .solver import Solver


def parse_csv(csv_file):
    # TODO: Size verification
    try:
        reader = csv.reader(open(csv_file, "r"))
        list_matrix = []
        matrix = []
        for line in reader:
            row = []
            for item in line:
                row.append(int(item))
            matrix.append(row)
            if len(matrix) == 9:
                list_matrix.append(matrix)
                matrix = []
        return list_matrix
    except FileNotFoundError as e:
        print(e)
    except MalformedSudokuException as e:
        print(e)


def parse_array_to_csv(list_matrix, filename):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for matrix in list_matrix:
            for row in matrix:
                writer.writerow(row)


def solve():
    resolved_matrix = []
    try:
        list_matrix = parse_csv("../../resources/sudokuChain.csv")
        for matrix in list_matrix:
            solver = Solver(matrix)
            solver.solve()
            resolved_matrix.append(solver.get_matrix())
        parse_array_to_csv(resolved_matrix, "../../resources/asd.csv")
    except KeyboardInterrupt:
        parse_array_to_csv(resolved_matrix, "../../resources/save.csv")


# TODO: Interaccion con usuario
def sudoku_solve():
    pass


if __name__ == '__main__':
    solve()
