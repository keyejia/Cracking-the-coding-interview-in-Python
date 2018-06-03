import unittest
def rotate_matrix(m):
    l = len(m)
    rotate = [None]*l
    for row in range (0,l):
        rotate[row] = [None]*l
    for i in range (0, l):
        for j in range (0, l):
            rotate[l-i-1][j] = m[j][i]
    
    return rotate
    
class Test(unittest.TestCase):
  def test_rotate_matrix(self):
    mat1 = [[1,2],[3,4]]
    mat2 = [[2,4],[1,3]]
    self.assertEqual(rotate_matrix(mat1), mat2)
    mat3 = [[1,2,3],[4,5,6],[7,8,9]]
    mat4 = [[3,6,9],[2,5,8],[1,4,7]]
    self.assertEqual(rotate_matrix(mat3), mat4)
    mat5 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    mat6 = [[4,8,12,16],[3,7,11,15],[2,6,10,14],[1,5,9,13]]
    self.assertEqual(rotate_matrix(mat5), mat6)

unittest.main()
