"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character but a
character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
"""

#=> first we check whether both strings have same length or not
#=> next we see if both strings have same number of distinct characters or not. We check
#   this using two dictionaries and then comparing their length
#=> at last we need to see whether each same character in string A corresponds to a
#   same character in the string B.
#   example1: A: paper   B: title   True
#               p   ->  t
#               a   ->  i
#               p   ->  t
#               e   ->  l
#               r   ->  e
#            look how both 'p' corresponds to 't'
#   example2: A: aba    B: baa      False
#               a   ->  b
#               b   ->  a
#               a   ->  a
#            look how one 'a' corresponds to 'b' and another 'a' corresponds to 'b'

def isIsomorphic(s, t):
    if len(s)!=len(t):
        return False
    hash1 = {}
    hash2 = {}
    for i in range(len(s)):
        if s[i] in hash1.keys():
            if t[i] not in hash1[s[i]]:
                return False
        else:
            hash1.update({s[i]:t[i]})
        hash2.update({t[i]:True})
    if len(hash1)!=len(hash2):
        return False
    return True

print isIsomorphic("paper","title")
print isIsomorphic("aba","baa")