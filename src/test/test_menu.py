from unittest import TestCase, mock
from src.main.menu import Menu
from src.main.logic import Menu


class TestMenu(TestCase):
    def setUp(self):
        self.menu = Menu()

    def test_validInput(self):
        with mock.patch('builtins.input', return_value=1):
            assert self.menu.show_options() == 1
        with mock.patch('builtins.input', return_value=2):
            assert self.menu.show_options() == 2
        with mock.patch('builtins.input', return_value=3):
            assert self.menu.show_options() == 3

    def test_invalidInput(self):
        self.menu.show_options()
        TestCase().assertRaises(expected_exception=ValueError)


if __name__ == '__main__':
    TestMenu().test_validInput()
