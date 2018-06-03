import unittest

def is_rotation(stringA,stringB):
    if len(stringA) != len(stringB):
        return False
    else:
        return is_substring(stringA + stringA, stringB)

        
def is_substring(stringA, stringB):
    lenA = len(stringA)
    lenB = len(stringB)
    for i in range(0,lenA-lenB+1):
        if stringA[i:i+lenB] == stringB:
            return True
    return False
            
class Test(unittest.TestCase):
  def test_is_rotation(self):
    s1 = "tabletop"
    s2 = "toptable"
    s3 = "optalbet"
    self.assertTrue(is_rotation(s1, s2))
    self.assertFalse(is_rotation(s1, s3))
  
  def test_is_substring(self):
    s1 = "cat in the hat"
    s2 = "cat"
    s3 = "hat"
    s4 = "cats"
    self.assertTrue(is_substring(s1, s2))
    self.assertTrue(is_substring(s1, s3))
    self.assertFalse(is_substring(s1, s4))

unittest.main()
