import csv

from src.exception.input_exception import *


def parse_csv_to_array(csv_file):
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


def solve(path):
    matrix = parse_csv_to_array(path)


if __name__ == '__main__':
    m = parse_csv_to_array("../../resources/sudokus.csv")
    print(m)
