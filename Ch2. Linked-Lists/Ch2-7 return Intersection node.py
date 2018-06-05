# -*- coding: utf-8 -*-
import unittest

def intersection(head1, head2):
    A = {}
    while head1:
        A[head1] = 1
        head1= head1.next
    while head2:
        if head2 in A:
            return head2
        head2 = head2.next
    return None
    
    
class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_intersection(self):
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    self.assertEqual(intersection(head1, head2), None)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    self.assertEqual(intersection(head3, head4), node)

unittest.main()
