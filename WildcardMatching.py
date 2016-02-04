"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false
"""

#=> set i for position at string1 and j for position at string2
#=> if char at i matches char at j or char at j is '?' then advance both i and j
#=> if char at position j is '*' then we mark this position as startIndex, the
#   next position to it as j (because in following iterations we need to check
#   whether the next char to '*' in j matches to char at i) and we mark corresponding
#   i position as iIndex
#=> if starIndex!=-1 that means we are still matching with start therefore j = starIndex+1
#   i = iIndex+1 and we increment iIndex because this keeps the track of the last i position
#   matched with '*'

def isMatch(s, p):
    i = 0
    j = 0
    starIndex = -1
    iIndex = -1
    while i<len(s):
        """try:
            print i,j,starIndex,iIndex,s[i],p[j]
        except IndexError:
            pass"""
        if j<len(p) and (s[i]==p[j] or p[j]=='?'):
            i += 1
            j += 1
        elif j<len(p) and p[j]=='*':
            starIndex = j
            iIndex = i
            j += 1
        elif starIndex!=-1:
            j = starIndex + 1
            #i += 1
            i = iIndex+1
            iIndex += 1
        else:
            return False
    while j<len(p) and p[j]=='*':
        j += 1
    return j==len(p)

print isMatch("hhhhhhhi","*hi")