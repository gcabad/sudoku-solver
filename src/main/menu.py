"""
Menú:
El usuario debe contar con las siguientes opciones:
1- ingresar el nombre de un archivo (path completo) con la entrada de datos
2- Guardar la ejecución parcial, con un nombre arbitrario
3- Recuperar una ejecución parcial y continuarla.
"""
from src.exception.input_exception import InputException

from src.main.logic import parse_csv_to_array

from src.main.logic import solve


class Menu(object):

    def show_menu(self):
        menu = "Para resolver un sudoku:\n" \
               "Ingrese el nombre de un nuevo sudoku, o uno anteriormente guardado\n" \
               "Para interrumpir la ejecucion y guardarla, ingrese el comando CTRL + C"
        solve(input(menu))
