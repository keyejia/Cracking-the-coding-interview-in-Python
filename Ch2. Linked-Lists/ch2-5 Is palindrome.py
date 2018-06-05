import unittest

def is_palindrome(head):
    node1 = head
    node2 = copy_reverse(head)
    while node1:
        if node1.data != node2.data:
            return False
        node1 = node1.next
        node2 = node2.next
    return True
        
def copy_reverse(head):
    firstnode = copy(head)
    secondnode = None
    while firstnode:
        temp = copy(firstnode.next)
        firstnode.next = secondnode
        secondnode = firstnode
        firstnode = temp
    return secondnode
      
def copy(node):
    if node == None: return None
    return Node(node.data, node.next)

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_palindrome(self):
    list1 = Node(10)
    self.assertTrue(is_palindrome(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(is_palindrome(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(is_palindrome(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(is_palindrome(list4))
    
  def test_copy_reverse(self):
    head = Node(10,Node(20,Node(30,Node(40))))
    self.assertEqual(str(copy_reverse(head)), "40,30,20,10")

unittest.main()