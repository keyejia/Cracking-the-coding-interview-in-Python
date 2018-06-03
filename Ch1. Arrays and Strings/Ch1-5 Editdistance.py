# -*- coding: utf-8 -*-
def isDistanceLessThanTwo(stringA, stringB):
    
    lenA = len(stringA)
    lenB = len(stringB)
    dis = 0
    if abs(lenA-lenB)>1:
        return False
    if stringA == stringB:return True
    if lenA == lenB:
        for i in range(0,lenA):
            if stringA[i]!=stringB[i]:
                dis += 1
                if dis > 1:
                    return False
        return True
    else:
        if lenA > lenB:
            shortS = stringB
            longS = stringA
        else:
            shortS = stringA
            longS = stringB
        for i in range(0,len(longS)):
            temp = longS[:i] + longS[i+1:]
            if temp == shortS:
                return True
            return False
            
print (isDistanceLessThanTwo('aaa', 'aaaa'))
print (isDistanceLessThanTwo('aaa', 'aaaaa'))
print (isDistanceLessThanTwo('aaa', 'aabb'))
print (isDistanceLessThanTwo('aaa', 'bbbb'))
print (isDistanceLessThanTwo('', ''))
print (isDistanceLessThanTwo('aaaa', 'aaba'))
print (isDistanceLessThanTwo('aaaa', 'babb'))


