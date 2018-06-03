# -*- coding: utf-8 -*-
def isPerOfPalindrome(stringA):
    Letters = {}
    for char in stringA:
        if char in Letters:
            Letters[char] += 1
        else:
            Letters[char] = 1
    odd = 0
    for count in Letters.values():
        if count%2 > 0:
            odd += 1
            if odd > 1:
                return False
    return True

    
print (isPerOfPalindrome('racecar'))
print (isPerOfPalindrome('recar'))
print (isPerOfPalindrome('rcecar'))
print (isPerOfPalindrome('rr'))
print (isPerOfPalindrome(''))

                        
