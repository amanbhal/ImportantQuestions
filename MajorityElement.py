"""
Given an array of size n, find the majority element. The majority element is the element that appears more than
floor(n/2)  times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

#=> Use Majority Vote algorithm.
#   We will sweep down the sequence starting at the pointer position shown above.
#   As we sweep we maintain a pair consisting of a current candidate and a counter. Initially, the current candidate
#   is unknown and the counter is 0.
#   When we move the pointer forward over an element e:
#       If the counter is 0, we set the current candidate to e and we set the counter to 1.
#       If the counter is not 0, we increment or decrement the counter according to whether e is the current candidate.
#   When we are done, the current candidate is the majority element, if there is a majority. To check whether the
#   current element is majority or not we find its count. It the count is greater than len(arr)/2 then it is majoruty
#   element otherwise there is no majority element in the array

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==0:
        return None
    elementCount = 0
    majorityElement = 0
    for i in range(len(nums)):
        if elementCount==0:
            elementCount = 1
            majorityElement = nums[i]
        else:
            if majorityElement==nums[i]:
                elementCount += 1
            else:
                elementCount -= 1
    #now check whether the element retrieved from previous iteration is actually majority element or not.
    count = 0
    for i in nums:
        if i==majorityElement:
            count += 1
    if count>len(nums)/2:
        return majorityElement
    else:
        return None
