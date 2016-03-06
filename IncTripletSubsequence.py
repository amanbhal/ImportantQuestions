"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""


#=> DP solution same as increasing subsequence problem. O(n^2) time and O(n) space.
def increasingTriplet1(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums)==0 or len(nums)<3:
        return False
    dp = [1 for i in range(len(nums))]
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = dp[j]+1
                if dp[i]>=3:
                    return True
    return False


#=> using two variables. O(n) time and O(1) space.
import sys
def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums)==0 or len(nums)<3:
        return False
    small = sys.maxint
    big = sys.maxint
    for i in range(len(nums)):
        if nums[i]<=small:
            small = nums[i]
        elif nums[i]<=big:
            big = nums[i]
        else:
            return True
    return False