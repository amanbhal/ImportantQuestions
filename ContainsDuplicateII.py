"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if len(nums)==0:
        return False
    duplicate = {}
    for i in range(len(nums)):
        if nums[i] in duplicate:
            if abs(duplicate[nums[i]][0]-i)<=k:
                return True
            else:
                duplicate[nums[i]] = [i]
        else:
            duplicate[nums[i]] = [i]
    return False