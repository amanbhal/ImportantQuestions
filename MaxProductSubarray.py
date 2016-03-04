"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

#=> Using Dynamic Programming
#=> at each index in nums we will check the local maximum and local minimum from previous maximum, previous minimum and
#   current nums

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==0:
        return 0
    maximum = [None for i in range(len(nums))]
    minimum = [None for i in range(len(nums))]
    maximum[0] = nums[0]
    minimum[0] = nums[0]
    result = nums[0]
    for i in range(1,len(nums)):
        maximum[i] = max(maximum[i-1]*nums[i],minimum[i-1]*nums[i],nums[i])
        minimum[i] = min(maximum[i-1]*nums[i],minimum[i-1]*nums[i],nums[i])
        result = max(result,maximum[i])
    return result

print maxProduct([2,3,-2,4])