import csv

from src.main.exception.exceptions import *
from src.main.solver import Solver


def parse_csv(csv_file):
    file = open(csv_file, "r")
    if not csv_file.endswith(".csv"):
        raise InvalidFileExtensionException("Introduzca un archivo de extension .csv")
    reader = csv.reader(file)
    list_matrix = []
    matrix = []
    for line in reader:
        row = []
        for item in line:
            row.append(int(item))
        matrix.append(row)
        if len(matrix) != 9 and len(matrix[0]) != 9:
            raise MalformedSudokuException("Introduzca un sudoku de tamaño 9x9")
        if len(matrix) == 9:
            list_matrix.append(matrix)
            matrix = []
    return list_matrix


def parse_array_to_csv(list_matrix, filename):
    with open(filename, "w+", newline='') as file:
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
        file_name = input("Ejecucion interrumpida.\n"
                          "Introduzca nombre del archivo donde quiera guardar la ejecucion parcial")
        parse_array_to_csv(save_parcial(resolved_matrix, list_matrix), "resources/" + file_name + ".csv")


# TODO: iterar lista de n, guardar posicion si se corta, clone el archivo y que reemplaze lo resuelto
def solve_empty(n):
    try:
        solver = Solver(create_empty_matrix(n))
        solver.solveEmpty(n)
        # TODO: imprimir tablita
        solver.get_matrix()
    except KeyboardInterrupt:
        parse_array_to_csv(solver.get_matrix(), "resources/Parcial.csv")


def save_parcial(solved, not_solved):
    parcial_list = solved[:]
    for x in range(len(solved), len(not_solved)):
        parcial_list.append(not_solved[x])
    return parcial_list


def create_empty_matrix(n):
    matrix = []
    for _ in range(1, n + 1):
        row = []
        for _ in range(1, n + 1):
            row.append(0)
        matrix.append(row)
    return matrix


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
            try:
                solve_path(file_path)
            except MalformedSudokuException as e:
                print("\x1b[31m" + str(e) + "\x1b[39m")
                continue
            except FileNotFoundError as e:
                print("\x1b[31m" + str(e.strerror) + "\x1b[39m")
                continue
            except InvalidFileExtensionException as e:
                print("\x1b[31m" + str(e) + "\x1b[39m")
                continue
            print("Finalizado.")
            break
        elif choice1 == "2":
            print("elegiste 2")
        elif choice1 == "3":
            n = input("Comenzaremos a resolver un sudoku de N cosos. Por favor, inserte el numero de cosos.")
            # TODO: Devolver tabla y funcionar con N cosos
            solve_empty(n)
        elif choice1 == "4":
            print("Sudoku solver realizado por Toloza, Tomas y Abad, Gonzalo.")
        elif choice1 == "5" or choice1 == "salir":
            exit()
        else:
            print("Por favor, introduzca una opción valida.")


if __name__ == '__main__':
    sudoku_solve()
