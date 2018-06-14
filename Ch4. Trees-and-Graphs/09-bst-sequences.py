# Enumerate all inserrtion sequences that could have led to the given BST.

def bst_sequences(bst):
  return bst_sequences_partial([], [bst])
  
def bst_sequences_partial(partial, subtrees):
  if not subtrees:
      return [partial]
  sequence = []
  for i, node in enumerate(subtrees):
      nextPartial = partial+[node.data]
      nextSubtree = subtrees[:i] + subtrees[i+1:]
      if node.left:
          nextSubtree.append(node.left)
      if node.right:
          nextSubtree.append(node.right)
      sequence += bst_sequences_partial(nextPartial, nextSubtree)
  return sequence 
  
class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
  
import unittest

class Test(unittest.TestCase):
  def test_bst_sequences(self):
    self.assertEqual(bst_sequences(Node(7,Node(4,Node(5)),Node(9))), [
      [7, 4, 9, 5],
      [7, 4, 5, 9],
      [7, 9, 4, 5]])
    self.assertEqual(bst_sequences(Node(7,Node(4,Node(5),Node(6)),Node(9))), [
      [7, 4, 9, 5, 6],
      [7, 4, 9, 6, 5],
      [7, 4, 5, 9, 6],
      [7, 4, 5, 6, 9],
      [7, 4, 6, 9, 5],
      [7, 4, 6, 5, 9],
      [7, 9, 4, 5, 6],
      [7, 9, 4, 6, 5]])


if __name__ == "__main__":
  unittest.main()

