from unittest import TestCase

import src.main.logic as logic
from src.main.exception.exceptions import *


class TestLogic(TestCase):

    def test_parse_input_file(self):
        self.assertRaises(MalformedSudokuException, logic.parse_csv("resources/malformed_sudoku.csv"))

    def test_interrupd(self):
        logic.solve_path("resources/sudokuChain.csv")

    def test_parcial_save_round_matrix(self):
        logic.solve_path("resources/interrupted.csv")
        TestCase().assertEquals(logic.parse_csv("resources/archivo_resuelto.csv"), logic.parse_csv("resources/solved.csv"))

    def test_parcial_save_inpair_matrix(self):
        logic.solve_path("resources/falopita.csv")
        TestCase().assertEquals(logic.parse_csv("resources/archivo_resuelto.csv"), logic.parse_csv("resources/solved.csv"))
