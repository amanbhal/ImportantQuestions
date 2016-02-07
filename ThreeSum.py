"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique
triplets in the array which gives the sum of zero.

Note:

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)


"""

#=> sort the array then for each element call twoSum on nums[i+1:]. Now because we need all the triplets
#   that sum up to zero therefore inside twoSum method maintain a list and add elements into that list whenever
#   a match is found.

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums)<3:
        return []
    nums.sort()
    result = []
    for i in range(len(nums)):
        temp = twoSum(nums[i+1:],-nums[i])
        #print nums[i],temp
        if temp:
            for j in range(len(temp)):
                temp[j] = temp[j]+[nums[i]]
                temp[j].sort()
                #print temp[j]
                if temp[j] not in result:
                    result.append(temp[j])
    return result

def twoSum(nums, sum):
    #print nums
    if len(nums)<2:
        return False
    l = 0
    r = len(nums)-1
    localResult = []
    while l<r:
        if nums[l]+nums[r]==sum:
            localResult.append([nums[l],nums[r]])
            l += 1
            r -= 1
        elif nums[l]+nums[r]<sum:
            l += 1
        else:
            r -= 1
    if len(localResult)!=0:
        return localResult
    else:
        return False

print threeSum([-1,0,1,2,-1,-4])