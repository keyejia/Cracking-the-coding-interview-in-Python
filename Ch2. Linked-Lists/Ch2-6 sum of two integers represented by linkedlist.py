import unittest

def sum_lists(num1, num2):
    result = Node((num1.data+num2.data)%10)
    pA = result
    carry = int((num1.data+num2.data)/10)
    while num1 or num2:
        if num1:
            num1 = num1.next
            if num1:a = num1.data
            else: a = 0
        if num2:
            num2 = num2.next
            if num2:b = num2.data
            else: b = 0
        if num2 == None and num1 == None : break
        pA.next = Node((a+b+carry)%10)
        pA = pA.next
        carry = int((a+b+carry)/10)
        
    return result
    

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string
    
class Test(unittest.TestCase):
  def test_sum_lists(self):
    num1 = Node(1,Node(2,Node(3)))
    num2 = Node(4,Node(9,Node(5)))
    self.assertEqual(str(sum_lists(num1, num2)), "5,1,9")
    num1 = Node(9,Node(2,Node(3,Node(4,Node(1)))))
    num2 = Node(4,Node(9,Node(8)))
    self.assertEqual(str(sum_lists(num1, num2)), "3,2,2,5,1")

unittest.main()