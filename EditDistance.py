"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""

#=> Use Dynamic Programming
#   If current characters of two strings are same, nothing much to do. Ignore last characters and get count for
#   remaining strings. So we recur for lengths m-1 and n-1.
#   Else (If current characters are not same), we consider all operations on 'str1', consider all three operations
#   on current character of first string, recursively compute minimum cost for all three operations
#   and take minimum of three values.
#   Insert: Recur for m and n-1
#   Remove: Recur for m-1 and n
#   Replace: Recur for m-1 and n-1

def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    if len(word1)==0 and len(word2)==0:
        return 0
    if len(word1)==0:
        return len(word2)
    if len(word2)==0:
        return len(word1)
    distance = [[0 for i in range(len(word1)+1)] for i in range(len(word2)+1)]

    for i in range(len(word2)+1):
        for j in range(len(word1)+1):
            # If second string is empty, only option is to insert all characters of first string
            if i==0:
                distance[i][j] = j
            # If first string is empty, only option is to insert all characters of second string
            elif j==0:
                distance[i][j] = i
            # If last characters are same, ignore last char and recur for remaining string
            elif word1[j-1]==word2[i-1]:
                distance[i][j] = distance[i-1][j-1]
            # If last character are different, consider all possibilities and find minimum
            else:
                distance[i][j] = 1 + min(distance[i-1][j-1],    #Replace in word2
                                         distance[i-1][j],      #Remove from word2
                                         distance[i][j-1])      #Insert in word2

    return distance[len(word2)][len(word1)]

print minDistance("saturday","sunday")