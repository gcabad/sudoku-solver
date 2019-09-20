from unittest import TestCase

import logic as logic
from exception.exceptions import *


class TestLogic(TestCase):

    def test_parse_input_file(self):
        self.assertRaises(MalformedSudokuException, logic.parse_csv("resources/malformed_sudoku.csv"))

    def test_interrupd(self):
        logic.solve_path("resources/sudokuChain.csv")

    def test_parcial_save_round_matrix(self):
        logic.solve_path("resources/interrupted.csv")
        TestCase().assertEquals(logic.parse_csv("resources/archivo_resuelto.csv"),
                                logic.parse_csv("resources/solved.csv"))

    def test_parcial_save_inpair_matrix(self):
        logic.solve_path("resources/falopita.csv")
        TestCase().assertEquals(logic.parse_csv("resources/archivo_resuelto.csv"),
                                logic.parse_csv("resources/solved.csv"))

    def test_solve(self):
        logic.solve_path("resources/sudokuChain.csv")
        solved = logic.parse_csv("resources/archivo_resuelto.csv")
        expected = [[[9, 8, 4, 5, 7, 6, 2, 1, 3], [5, 1, 3, 4, 8, 2, 9, 6, 7], [7, 2, 6, 1, 3, 9, 5, 4, 8], [6, 3, 1, 9, 4, 7, 8, 5, 2], [4, 9, 5, 2, 6, 8, 3, 7, 1], [8, 7, 2, 3, 5, 1, 6, 9, 4], [2, 5, 7, 6, 1, 3, 4, 8, 9], [3, 6, 8, 7, 9, 4, 1, 2, 5], [1, 4, 9, 8, 2, 5, 7, 3, 6]], [[2, 4, 3, 9, 5, 8, 6, 7, 1], [7, 8, 9, 6, 1, 2, 4, 3, 5], [1, 6, 5, 7, 3, 4, 9, 2, 8], [4, 1, 7, 2, 6, 3, 8, 5, 9], [3, 9, 8, 5, 4, 7, 2, 1, 6], [6, 5, 2, 8, 9, 1, 3, 4, 7], [5, 7, 4, 3, 8, 9, 1, 6, 2], [9, 3, 6, 1, 2, 5, 7, 8, 4], [8, 2, 1, 4, 7, 6, 5, 9, 3]], [[2, 7, 4, 6, 3, 5, 8, 9, 1], [6, 8, 5, 7, 9, 1, 4, 3, 2], [9, 1, 3, 2, 4, 8, 5, 6, 7], [4, 3, 2, 5, 6, 7, 9, 1, 8], [1, 5, 9, 4, 8, 3, 2, 7, 6], [8, 6, 7, 1, 2, 9, 3, 5, 4], [7, 9, 1, 8, 5, 4, 6, 2, 3], [5, 4, 6, 3, 1, 2, 7, 8, 9], [3, 2, 8, 9, 7, 6, 1, 4, 5]], [[2, 8, 6, 1, 5, 4, 7, 9, 3], [7, 5, 4, 3, 9, 2, 8, 6, 1], [3, 1, 9, 6, 8, 7, 2, 5, 4], [9, 6, 2, 8, 4, 5, 1, 3, 7], [8, 4, 3, 7, 6, 1, 5, 2, 9], [1, 7, 5, 2, 3, 9, 4, 8, 6], [4, 9, 8, 5, 1, 6, 3, 7, 2], [6, 3, 7, 4, 2, 8, 9, 1, 5], [5, 2, 1, 9, 7, 3, 6, 4, 8]], [[1, 3, 7, 5, 2, 4, 8, 6, 9], [8, 5, 4, 3, 9, 6, 2, 1, 7], [6, 9, 2, 8, 7, 1, 3, 5, 4], [3, 1, 8, 4, 6, 7, 5, 9, 2], [2, 7, 6, 1, 5, 9, 4, 8, 3], [9, 4, 5, 2, 3, 8, 1, 7, 6], [5, 6, 3, 7, 8, 2, 9, 4, 1], [7, 2, 1, 9, 4, 5, 6, 3, 8], [4, 8, 9, 6, 1, 3, 7, 2, 5]], [[1, 6, 4, 2, 8, 3, 5, 7, 9], [3, 8, 9, 5, 4, 7, 1, 2, 6], [5, 2, 7, 9, 1, 6, 3, 8, 4], [4, 9, 2, 6, 3, 5, 8, 1, 7], [7, 3, 8, 4, 2, 1, 9, 6, 5], [6, 1, 5, 7, 9, 8, 2, 4, 3], [2, 5, 6, 8, 7, 9, 4, 3, 1], [9, 4, 1, 3, 6, 2, 7, 5, 8], [8, 7, 3, 1, 5, 4, 6, 9, 2]]]
        TestCase().assertEqual(solved, expected)
        print("OK.")

    def test_not_equals_solutions(self):
        empty = logic.solve_empty(3)
        for num in range(len(empty)):
            for num2 in range(num + 1, len(empty)):
                TestCase().assertNotEqual(empty[num], empty[num2])
        print("OK.")

if __name__ == '__main__':
    test = TestLogic()
    # test.test_parse_input_file()
    # test.test_interrupd()
    # test.test_parcial_save_round_matrix()
    # test.test_parcial_save_inpair_matrix()
    test.test_solve()
    test.test_not_equals_solutions()
