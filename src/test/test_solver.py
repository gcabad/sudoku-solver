import math
from unittest import TestCase

from src.main.solver import Solver
import numpy as np
from src.main.logic import *


class SolverTest(TestCase):

    def setUp(self):
        pass

    def test_not_null(self):
        test_sudoku = [[0,8,0,5,7,6,2,0,0],
                 [0,0,0,4,0,2,0,0,0],
                 [0,0,0,0,3,9,5,4,8],
                 [6,3,0,9,0,0,8,5,2],
                 [0,9,0,2,0,0,3,7,0],
                 [8,0,0,0,5,0,6,9,4],
                 [2,5,7,6,0,3,4,8,9],
                 [3,0,8,7,0,0,0,2,5],
                 [0,4,0,0,0,0,0,0,6]]
        first = []
        for x in test_sudoku:
            a = x[:]
            first.append(a)
        self.solver = Solver(test_sudoku)
        self.solver.solve()
        last = self.solver.get_matrix()
        print(first)
        assert first != last

    def test_solve_empty_9x9(self):
        empty = create_empty_matrix(9)
        self.solver = Solver(empty)
        self.solver.solve_empty()
        print(self.solver.get_matrix())

    def test_solve_empty_16x16(self):
        empty = create_empty_matrix(16)
        self.solver = Solver(empty)
        self.solver.solve_empty()
        print(np.matrix(self.solver.get_matrix()))

    def test_10_solution(self):
        empty = create_empty_matrix(9)
        self.solver = Solver(empty)
        self.solver.solve_empty()

        print(len(self.solver.solutions))
        solutions = []
        for matrix in self.solver.solutions:
            if matrix not in solutions:
                solutions.append(matrix)