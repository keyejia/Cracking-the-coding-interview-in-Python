# Tell whether or not a binary tree is balanced.

def is_balanced(binary_tree):
  if not binary_tree:
    return (True, 0)
  left_balance, left_depth = is_balanced(binary_tree.left)
  if not left_balance:
    return (False, None)
  right_balance, right_depth = is_balanced(binary_tree.right)
  if not right_balance or abs(right_depth-left_depth) > 1:
    return (False, None)
  return (True, max(right_depth, left_depth)+1)

class Node():
  def __init__(self, left=None, right=None):
    self.left, self.right = left, right

import unittest

class Test(unittest.TestCase):
  def test_is_balanced(self):
    self.assertEqual(is_balanced(Node(Node(),Node())), (True, 2))
    self.assertEqual(is_balanced(Node(Node(),Node(Node()))), (True, 3))
    self.assertEqual(is_balanced(Node(Node(),Node(Node(Node())))),
        (False, None))
    self.assertEqual(is_balanced(Node(Node(Node()),Node(Node(Node())))),
        (False,None))
    self.assertEqual(is_balanced(Node(Node(Node()),
        Node(Node(Node()),Node()))), (True, 4))

if __name__ == "__main__":
  unittest.main()
