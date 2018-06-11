# Find the first common ancestor of two nodes in a tree.

def first_common_ancestor(node1, node2):
  

class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.parent = None
    if self.left:
      self.left.parent = self
    if self.right:
      self.right.parent = self

import unittest

class Test(unittest.TestCase):
  def test_first_common_ancestor(self):
    node1 = Node(11, Node(55), Node(77, Node(44)))
    node2 = Node(22, Node(99))
    self.assertEqual(first_common_ancestor(node1, node2), None)
    node3 = Node(33, node1, Node(88, Node(123, None, node2)))
    node4 = Node(44, node3, Node(66))
    self.assertEqual(first_common_ancestor(node1, node2), node3)

if __name__ == "__main__":
  unittest.main()
