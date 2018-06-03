# -*- coding: utf-8 -*-
import unittest
def zero_out_row_col(m):
    h = len(m)
    l = len(m[0])
    ipositions = {}
    jpositions = {}
    
    for i in range (0, h):
        for j in range(0, l):
            if m[i][j] == 0:
                ipositions[i] = 1
                jpositions[j] = 1
    
    for i in ipositions.keys():
        for j in range (0, l):
            m[i][j] = 0
    for j in jpositions.keys():
        for i in range (0, h):
            m[i][j] = 0

class Test(unittest.TestCase):
  def test_zero_out_row_col_matrix(self):
    mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
    mat2 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[2,0,4,0,6]]
    zero_out_row_col(mat1)
    self.assertEqual(mat1, mat2)

    mat1 = [[1,1,1],[1,0,1],[1,1,1]]
    mat2 = [[1,0,1],[0,0,0],[1,0,1]]
    zero_out_row_col(mat1)
    self.assertEqual(mat1, mat2)
    
unittest.main()