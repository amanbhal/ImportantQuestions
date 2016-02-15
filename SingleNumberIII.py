"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

#=> Using Bit Manipulation

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    #first time get the bits of two numbers appearing only once.
    x = 0
    result = []
    for i in nums:
        x = x^i
    #now find a bit that is different in both so that we can seperate them.
    uniqueBit = (x&(x-1))^x
    num1 = num2 = 0
    for i in nums:
        if i&uniqueBit:
            num1 = num1^i
        else:
            num2 = num2^i
    return [num1,num2]

print singleNumber([1, 2, 1, 3, 2, 5])