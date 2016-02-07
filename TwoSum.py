"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

"""

#=> Method 1
#       first sort the array and then apply two pointers method. This is slow because we have to sort first

#=> Method 2
#       Using a hashmap to store target-nums[i] and index i for each element.

def twoSumWithHashmap(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash = {}
    for i in range(len(nums)):
        #check if the nums[i] is in the hashmap i.e. it's pairing element is also present. If not present then
        #store target-numm[i] with value i
        if nums[i] not in hash:
            hash[target-nums[i]] = i
        else:
            return sorted([hash[nums[i]]+1,i+1])

def twoSumWithSorting(nums, target):
    x = sorted(nums)
    f = 0
    l = len(x)-1
    while f<=l:
        if x[f]+x[l]==target:
            break
        elif x[f]+x[l]<target:
            f += 1
        else:
            l -= 1
    a = nums.index(x[f])
    nums[a] = None
    b = nums.index(x[l])
    if a<b:
        return [a+1,b+1]
    else:
        return [b+1,a+1]

print twoSumWithHashmap([2,7,11,15],9)
print twoSumWithSorting([-1,-2,-3,-4,-5,-6,-7,-8],-9)