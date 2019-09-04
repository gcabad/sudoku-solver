from unittest import TestCase

import src.main.logic as logic


class TestGetMenuInput(TestCase):

    def test_parse_input_file(self):
        logic.parse_csv()
