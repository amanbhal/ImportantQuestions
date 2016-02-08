"""
Given an array arr[] of integers, find out the difference between any two elements such that larger element
appears after the smaller number in arr[].

Examples: If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8 (Diff between 10 and 2).
If array is [ 7, 9, 5, 6, 3, 2 ] then returned value should be 2 (Diff between 7 and 9)
"""

#=> maintain a maxDiffernce variable storing max difference seen so far and another varible called
#   minSoFar holding the minimum value seen so far.

import sys
def findMax(A):
    if len(A)==0:
        return null
    if len(A)==1:
        return A[0]
    maxDiff = -sys.maxint
    minSoFar = A[0]
    for i in range(1,len(A)):
        if A[i]-minSoFar>maxDiff:
            maxDiff = A[i]-minSoFar
        if A[i]<minSoFar:
            minSoFar = A[i]
    return maxDiff

print findMax([691,692,693,694,695,40,535])