from unittest import TestCase

import src.main.logic as e


class TestGetMenuInput(TestCase):

    def test_parse_input_file(self):
        matrix = e.parse_csv(e.parse_csv("resources/sudokus.csv"))
        print(matrix)
