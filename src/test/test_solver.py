import math
from unittest import TestCase

from src.main.solver import Solver
import numpy as np
from src.main.logic import *


class SolverTest(TestCase):

    def setUp(self):
        pass

 #   def test_not_null(self):
 #       first = self.solver.get_matrix()
 #       self.solver.solve()
 #       last = self.solver.get_matrix()
 #       assert first != last

 #   def test_solve_empty(self):
 #       empty = create_empty_matrix(16)
 #       self.solver = Solver(empty)
 #       self.solver.solve_empty()
 #       print(np.matrix(self.solver.get_matrix()))

#    def test_solve_empty_32(self):
 #       empty = create_empty_matrix(25)
  #      self.solver = Solver(empty)
   #     self.solver.solve()
   #     print(np.matrix(self.solver.get_matrix()))

    def test_solve_empty_9(self):
        empty = create_empty_matrix(16)
        self.solver = Solver(empty)
        self.solver.solve_empty()
        print(len(self.solver.solutions))
        list = []
        for x in self.solver.solutions:
            if x not in list:
                list.append(x)
            else:
                print("Repetido")
        print("List len: " + str(len(list)) + ". \nSolutions len: " +str(len(self.solver.solutions)))

