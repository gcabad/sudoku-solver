from unittest import TestCase, mock
from src.exception.input_exception import InputException

import src.main.logic as e


class TestGetMenuInput(TestCase):

    def test_parse_input_file(self):
        matrix = e.parse_csv_to_array(e.parse_csv_to_array("resources/sudokus.csv"))
        print(matrix)
