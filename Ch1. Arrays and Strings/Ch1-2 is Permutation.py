from collections import Counter

def isPermutation(stringA, stringB):
  return Counter(stringA) == Counter(stringB)

print (isPermutation('abc','cba'))
print (isPermutation('abc','bca'))
print (isPermutation('abc','bcaa'))
print (isPermutation('abc','bcax'))
print (isPermutation('abc','b'))