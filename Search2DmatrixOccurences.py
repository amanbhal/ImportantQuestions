"""
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.
example:
[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.
"""

def searchMatrix(matrix, target):
    # write your code here
    if len(matrix)==0:
        return 0
    x = 0
    y = len(matrix[0])-1
    count = 0
    while inBound(x,y,matrix):
        if matrix[x][y]==target:
            count += 1
            y -= 1
        elif matrix[x][y]<target:
            x += 1
        else:
            y -= 1
    return count

def inBound(x,y,matrix):
    if x<0 or y<0:
        return False
    if x>=len(matrix) or y>=len(matrix[0]):
        return False
    return True

print searchMatrix([[1, 3, 5, 7],[2, 4, 7, 8],[3, 5, 9, 10]],3)