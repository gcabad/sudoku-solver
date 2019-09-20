import csv
import sys
import time

from exception.exceptions import *
from solver import Solver
from table import Table

table = Table()


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
    file.close()
    return list_matrix


def parse_array_to_csv(list_matrix, filename):
    with open(filename, "w+", newline='') as file:
        writer = csv.writer(file)
        for matrix in list_matrix:
            for row in matrix:
                writer.writerow(row)


def solve_path(path):
    try:
        resolved_matrix = []
        list_matrix = parse_csv(path)
        for matrix in enumerate(list_matrix):
            solver = Solver(matrix[1])
            print("Resuelta matriz " + str(
                matrix[0] + 1) if solver.solve() else "No se pudo resolver la matriz " + str(matrix[0] + 1))
            resolved_matrix.append(solver.get_matrix())
        parse_array_to_csv(resolved_matrix, "resources/archivo_resuelto.csv")
    except KeyboardInterrupt:
        file_name = input("Ejecucion interrumpida.\n"
                          "Introduzca path donde quiera guardar la ejecucion parcial\n")
        parse_array_to_csv(save_parcial(resolved_matrix, parse_csv(path)), file_name)


def solve_empty(r):
    try:
        start = time.time()
        solver = Solver(create_empty_matrix(r ** 2))
        solver.solve_empty()
        finish = time.time()
        time_taken = finish - start
        parse_array_to_csv(solver.solutions, 'resources/empty_sudoku_{}x{}_solutions.csv'.format(str(r ** 2), (r ** 2)))
        print(
            "Finalizado. Ver archivo con las distintas resoluciones en 'resources/empty_sudoku_{}x{}_solutions.csv'".format(
                str(r ** 2), (r ** 2)))
        print("Tambien puede ver la tabla con los tiempos en resources/lil_table.csv")
        table.append_table("{}    {}".format(str(r), round(time_taken, 3)))
    except KeyboardInterrupt:
        finish = time.time()
        time_taken = finish - start
        print("Ejecucion interrumpida en r = {}. Tiempo de ejecución tomado: {}".format(str(r), round(time_taken, 3)))


def save_parcial(solved, not_solved):
    parcial_list = solved[:]
    for x in range(len(solved), len(not_solved)):
        parcial_list.append(not_solved[x])
    return parcial_list


def create_empty_matrix(n):
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        matrix.append(row)
    return matrix


def print_error(error):
    print("\x1b[31m" + error + "\x1b[39m")


def sudoku_solve():
    # print("¡Bienvenido al Sudoku Solver!".center(60, "="))
    print(open("resources/bienvenida.txt", "r",encoding="utf8").read(), "\n")
    try:
        while True:
            print("Por favor, ingrese el número correspondiente a la opción que desea realizar:")
            choice1 = input("1) Resolver uno o varios tableros de sudoku en un archivo de formato CSV.\n"
                            "2) Continuar una ejecución parcial.\n"
                            "3) Resolver un sudoku en blanco.\n"
                            "4) Datos del grupo.\n"
                            "5) Salir.\n")
            if choice1 == "1":
                try:
                    file_path = input("Por favor, complete el path del archivo que desea utilizar:\n")
                    solve_path(file_path)
                except MalformedSudokuException as e:
                    print_error(str(e))
                    continue
                except FileNotFoundError as e:
                    print_error(str(e.strerror))
                    continue
                except InvalidFileExtensionException as e:
                    print_error(str(e))
                    continue
                except ValueError:
                    print_error("El sudoku contiene caracteres no numericos")
                    continue
                print("Finalizado. Ver archivo resuelto en 'resources/archivo_resuelto.csv'")
                continue
            elif choice1 == "2":
                try:
                    file_path = input("Por favor, complete el path del archivo que desea utilizar:\n")
                    solve_path(file_path)
                except MalformedSudokuException as e:
                    print_error(str(e))
                    continue
                except FileNotFoundError as e:
                    print_error(str(e.strerror))
                    continue
                except InvalidFileExtensionException as e:
                    print_error(str(e))
                    continue
                except ValueError:
                    print_error("El sudoku contiene caracteres no numericos")
                    continue
                print("Finalizado. Ver archivo resuelto en 'resources/archivo_resuelto.csv'")
                continue
            elif choice1 == "3":
                solve_empty_increment()
            elif choice1 == "4":
                # print("Sudoku solver realizado por Toloza, Tomas y Abad, Gonzalo.")
                printear_falopa()
            elif choice1 == "5" or choice1 == "salir":
                raise KeyboardInterrupt
            else:
                print("Por favor, introduzca una opción valida.")
    except KeyboardInterrupt:
        sys.exit()


def solve_empty_increment():
    for n in range(table.get_last_iteration(), 6):
        print("Resolviendo un sudoku de {}x{}".format(n, n))
        solve_empty(n)


def printear_falopa():
    print(open("resources/falopa.txt", "r").read())


if __name__ == '__main__':
    sudoku_solve()
