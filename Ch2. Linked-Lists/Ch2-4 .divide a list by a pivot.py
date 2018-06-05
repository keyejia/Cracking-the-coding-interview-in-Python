import unittest

def partition(head, p):
    node = head
    headA = None
    headB = None
    tailA = None
    while node:
        if node.data < p:
            if headA ==None:
                pA = node
                headA = pA
            else: 
                pA.next = node
                pA = pA.next
                tailA = node
        else:
            if headB == None:
                pB = node
                headB = pB
            else: 
                pB.next = node
                pB = pB.next
        node = node.next
    tailA.next = headB
    return headA
                


class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_partition(self):
    head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
    head2 = partition(head1, 6)
    self.assertEqual(str(head2), "2,1,3,7,9,6,8")
    head3 = partition(head2, 7)
    self.assertEqual(str(head3), "2,1,3,6,7,9,8")

unittest.main()