"""
Given an array of integers, every element appears three times except for one. Find that single one.
"""

#=> Using Bit Manipulation

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ones = twos = threes = 0
    for i in nums:
        #add the numbers appearing 2nd time to twos. (ones & i) will give the bits appearing 2nd time
        twos = twos | (ones & i)
        #add the numbers appearing for the first time to ones.
        ones = ones^i
        #add the numbers appearing for 3rd time to threes.
        threes = ones & twos
        #removes the numbers appearing 3rd time from ones and twos.
        ones = ones & ~threes
        twos = twos & ~threes
    return ones

print singleNumber([1,1,1,2,3,3,3])