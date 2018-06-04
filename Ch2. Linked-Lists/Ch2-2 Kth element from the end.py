# -*- coding: utf-8 -*-

import unittest


def kth_to_last(head, k):
    if k == 0: return None
    pA = head
    pB = head
    for i in range (0,k):
        if not pA:
            return None
        pA = pA.next
    while pA:
        pA, pB = pA.next, pB.next
    return pB

class Node():
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Test(unittest.TestCase):
  def test_kth_to_last(self):
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
    self.assertEqual(None, kth_to_last(head, 0));
    self.assertEqual(7, kth_to_last(head, 1).data);
    self.assertEqual(4, kth_to_last(head, 4).data);
    self.assertEqual(2, kth_to_last(head, 6).data);
    self.assertEqual(1, kth_to_last(head, 7).data);
    self.assertEqual(None, kth_to_last(head, 8));

unittest.main()