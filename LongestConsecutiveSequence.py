"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


#=> To run the program in O(1) time make use of Hash Table

import sys
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==0:
        return 0
    hashTable = {}
    for i in range(len(nums)):
        hashTable[nums[i]] = 0
    maxCount = -sys.maxint
    for i in range(len(nums)):
        x = nums[i]
        #if a value lower than x is present the let it make the consecutive sequence
        if (x-1) in hashTable:
            continue
        #else if a value lower than x is not present then consecutive sequence will start from x itself and will keep on increasing
        count = 1
        right = x+1
        while right in hashTable:
            count += 1
            right += 1
        #we record the length of this longest consecutive sequence achieved by x
        maxCount = max(maxCount,count)
    return maxCount

print longestConsecutive([100, 4, 200, 1, 3, 2])