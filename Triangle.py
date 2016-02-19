"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the
row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the
triangle.
"""

#=> make bottom up using 1-D array

def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    if len(triangle)==0:
        return 0
    result = triangle[-1]
    n = len(triangle[-1])
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            result[j] = triangle[i][j] + min(result[j],result[j+1])
    return result[0]

print minimumTotal([[3],[300,3],[3,200,300],[400,100,1,1]])