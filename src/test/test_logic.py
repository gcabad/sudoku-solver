from unittest import TestCase

import src.main.logic as logic
from src.main.exception.exceptions import *


class TestLogic(TestCase):

    def test_parse_input_file(self):
        self.assertRaises(MalformedSudokuException, logic.parse_csv("resources/malformed_sudoku.csv"))

    def test_read_table(self):
        logic.save_table([])
        print(logic.get_last_r())
