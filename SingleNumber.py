"""
Given an array of integers, every element appears twice except for one. Find that single one.
"""

#=> Using Bit Manipulation.

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    x = 0
    for i in nums:
        x = x^i
    return x

print singleNumber([1,2,1,3,3,4,4,5,5])