# -*- coding: utf-8 -*-

def noDupe(string):
  a={}
  for char in string:
    if char in a:
      return False
    else:
      a[char] = 1
  return True


print (noDupe('aaaaaa'))
print (noDupe('abcdefg'))
print (noDupe(''))
print (noDupe('abcdefghijklmnopqrstuvwxyzz'))
print (noDupe('abcdefghijklmnopqrstuvwxyz'))