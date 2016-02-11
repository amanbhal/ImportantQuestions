"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

#=> we will start the search from the top right corner.
#=> we will take the advantage of the fact that each row and col is sorted therefore at a position say [i][j]
#   if matrix[i][j]==target then return True
#   if matrix[i][j]<target then the bigger value can be found only at the following rows i.e. i+=1
#   if matrix[i][j]>target then the smaller value can be found only at preceeding cols i.e. j-=1

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    rows = len(matrix)
    if rows==0:
        return False
    cols = len(matrix[0])
    i = 0
    j = cols-1
    while i>=0 and i<rows and j>=0 and j<cols:
        if matrix[i][j]==target:
            return True
        elif matrix[i][j]<target:
            i += 1
        else:
            j -= 1
    return False

print searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],5)


print searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],20)