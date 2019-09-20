import math
import os
from unittest import TestCase

from solver import Solver
from logic import *


class SolverTest(TestCase):

    def setUp(self):
        pass

    def test_solved(self):
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
        TestCase().assertNotEqual(first,last)
        print("OK.")

    def test_solve_empty_9x9(self):
        empty = create_empty_matrix(9)
        self.solver = Solver(empty)
        self.solver.solve_empty()
        TestCase().assertIsNotNone(self.solver.solutions)
        print("OK.")

    def test_solve_empty_16x16(self):
        empty = create_empty_matrix(16)
        self.solver = Solver(empty)
        TestCase().assertIsNotNone(self.solver.solutions)
        print("OK.")

    def test_10_solution(self):
        empty = create_empty_matrix(9)
        self.solver = Solver(empty)
        self.solver.solve_empty()
        solutions = []
        for matrix in self.solver.solutions:
            if matrix not in solutions:
                solutions.append(matrix)
        TestCase().assertEqual(len(solutions), 10)
        print("OK.")

if __name__ == '__main__':
    SolverTest().test_solved()
    SolverTest().test_solve_empty_9x9()
    SolverTest().test_solve_empty_16x16()
    SolverTest().test_10_solution()
