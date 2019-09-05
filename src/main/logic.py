import csv

from src.main.exception.exceptions import *
from src.main.solver import Solver


def parse_csv(csv_file):
    try:
        reader = csv.reader(open(csv_file, "r"))
        list_matrix = []
        matrix = []
        for line in reader:
            row = []
            for item in line:
                row.append(int(item))
            matrix.append(row)
            if len(matrix) != 9 and len(matrix[0]) != 9:
                raise MalformedSudokuException
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


def solve_path(path):
    resolved_matrix = []
    try:
        list_matrix = parse_csv(path)
        for matrix in list_matrix:
            solver = Solver(matrix)
            solver.solve()
            resolved_matrix.append(solver.get_matrix())
        parse_array_to_csv(resolved_matrix, "resources/ArchivoResuelto.csv")
    except KeyboardInterrupt:
        parse_array_to_csv(resolved_matrix, "resources/Parcial.csv")


def solve_empty():
    resolved_matrix = []
    try:
        list_matrix = parse_csv("resources/emptySudoku.csv")
        for matrix in list_matrix:
            solver = Solver(matrix)
            solver.solveEmpty()
            resolved_matrix.append(solver.get_matrix())
        parse_array_to_csv(resolved_matrix, "resources/ArchivoResuelto.csv")
    except KeyboardInterrupt:
        parse_array_to_csv(resolved_matrix, "resources/Parcial.csv")


def sudoku_solve():
    print("¡Bienvenido al Sudoku Solver!".center(60, "="))
    print("Por favor, ingrese el número correspondiente a la opción que desea realizar:")
    while True:
        choice1 = input("1) Resolver uno o varios tableros de sudoku en un archivo de formato CSV.\n"
                        "2) Continuar una ejecución parcial.\n"
                        "3) Resolver un sudoku en blanco.\n"
                        "4) Datos del grupo.\n"
                        "5) Salir.\n")
        if choice1 == "1":
            file_path = input("Por favor, complete el path del archivo que desea utilizar:\n")
            solve_path(file_path)
            print("Finalizado.")
            break
        elif choice1 == "2":
            print("elegiste 2")
        elif choice1 == "3":
            n = input("Comenzaremos a resolver un sudoku de N cosos. Por favor, inserte el numero de cosos.")

            # Debería funcionar con N cosos.
            # Medio incheckeable

            solve_empty()
        elif choice1 == "4":
            print("Sudoku solver realizado por Toloza, Tomas y Abad, Gonzalo.")
        elif choice1 == "5" or choice1 == "salir":
            exit()
        else:
            print("Por favor, introduzca una opción valida.")


if __name__ == '__main__':
    sudoku_solve()
