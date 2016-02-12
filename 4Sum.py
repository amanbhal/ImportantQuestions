"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""

def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(nums)==0:
        return []
    uniqueElem = []
    nums.sort()
    for i in range(len(nums)-4):
        for j in range(i+1,len(nums)-3):
            num1 = nums[i]
            num2 = nums[j]
            left = j+1
            right = len(nums)-1
            while left<right:
                #print num1,num2,nums[left],nums[right],
                sum = num1+num2+nums[left]+nums[right]
                #print "sum=",sum
                temp = [num1,num2,nums[left],nums[right]]
                temp.sort()
                if sum==target:
                    if temp not in uniqueElem:
                        uniqueElem.append(temp)
                    left += 1
                    right -= 1
                elif sum>target:
                    right -= 1
                else:
                    left += 1
    return uniqueElem

print fourSum([-491,-477,-450,-436,-431,-410,-402,-402,-391,-381,-380,-377,-355,-346,-344,-325,-320,-318,-290,-286,-278,-278,-272,-261,-261,-259,-235,-234,-232,-220,-212,-206,-201,-196,-191,-186,-173,-164,-158,-133,-120,-98,-91,-87,-82,-73,-62,-55,-27,0,14,19,23,37,48,52,53,53,57,83,85,106,161,170,174,183,188,191,197,211,212,222,231,243,250,274,284,302,313,319,332,338,356,358,369,374,396,406,416,420,425,440,441,443,469,471,496],-2402)