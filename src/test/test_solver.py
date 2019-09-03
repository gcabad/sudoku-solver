from unittest import TestCase

from src.main.solver import Solver

from src.main.logic import *


class SolverTest(TestCase):

    def setUp(self):
        self.solver = Solver(parse_csv("../../resources/sudokus.csv"))

    def test_not_null(self):
        first = self.solver.get_matrix()
        self.solver.solve()
        last = self.solver.get_matrix()
        assert first != last
