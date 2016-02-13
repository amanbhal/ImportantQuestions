"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements
from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

example:    [1,2,3,0,0] m=3
            [4,5]       n=2
  result=>  [1,2,3,4,5]
"""

#=> As you can see in the example that there are trailing zeros in the first list which represents empty spaces.
#   Therefore we have to shift elements in first list to take these empty spaces.
#=> One good method to do this is to start from back i.e m-1 and n-1. Whichever of these is greater move it to
#   m+n-1 position in list1 and decrease the counter for that list.

def merge(A, m, B, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    while m>0 and n>0:
        if A[m-1]>B[n-1]:
            A[m+n-1] = A[m-1]
            m -= 1
        else:
            A[m+n-1] = B[n-1]
            n -= 1

    while n>0:
        A[m+n-1] = B[n-1]
        n -= 1

nums1 = [1,2,3,0,0]
merge(nums1,3,[4,5],2)
print nums1