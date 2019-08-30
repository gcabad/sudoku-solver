"""
Menú:
El usuario debe contar con las siguientes opciones:
1- ingresar el nombre de un archivo (path completo) con la entrada de datos
2- Guardar la ejecución parcial, con un nombre arbitrario
3- Recuperar una ejecución parcial y continuarla.
"""


class Menu(object):

    def show_options(self):
        menu = "Para resolver un sudoku:\n" \
               "Ingrese el nombre de un nuevo sudoku, o uno anteriormente guardado, o ingrese ENTER para resolver un sudoku vacio\n" \
               "Para interrumpir la ejecucion y guardarla, ingrese el comando CTRL + C\n"
        return input(menu)

    def show_savegame_not_found(self, filename):
        print("No se ha encontrado una partida con el nombre " + filename + ".\n" +
              "Leyendo sudokus.csv, creando partida con nombre " + filename + ".\n")

    def show_savegame_found(self, filename):
        print("Se ha encontrado una partida con el nombre " + filename + ".\n")

    def show_keyboard_interrupt(self, filename):
        print("Interrupcion de teclado ocurrida. Guardando progreso como " + filename)
