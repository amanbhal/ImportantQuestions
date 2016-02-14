"""
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
"""

#=> Analysis: the missing number can only be between 1 to len(A)+1. Therefore we can make use of the array itself
#   to store the numbers which are in this range at the index to which they belong.

def firstMissingPositive(A):
    i = 0
    while i<len(A):
        #if value is in the range
        if A[i]>0 and A[i]<len(A)+1:
            #if the value is at its correct position i.e. number 5 should be at index 4
            if A[i] == i+1:
                i += 1
            else:
                #if a number is not at its correct place but it is equal to the number at its correct place then
                #we move ahead. example [1,1,1] at index 1 and 2
                if A[i] == A[A[i]-1]:
                    i += 1
                #if the number is in the range and not at its correct place and the number at its correct place is
                #not equal to this number then we swap it with the number at its correct place
                else:
                    temp = A[A[i]-1]
                    A[A[i]-1] = A[i]
                    A[i] = temp
        #if the number is not in the range then we convert it to -1
        else:
            A[i] = -1
            i += 1
    #if we find -1 at position i then we return i+1
    missing = 1
    for i in range(len(A)):
        if A[i]!=missing:
            return missing
        else:
            missing += 1
    #if all the numbers are in the range then we return the number which is just greater than the last number
    #example: [1,1,1] it will return 2
    return missing

print firstMissingPositive([2,2])