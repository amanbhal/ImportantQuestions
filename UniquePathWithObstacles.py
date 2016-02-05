"""
Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,


There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]


The total number of unique paths is 2.

Note: m and n will be at most 100.

"""


def uniquePathsWithObstacles(obstacleGrid):
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    if obstacleGrid[0][0]==1 or obstacleGrid[rows-1][cols-1]==1:
        return 0
    matrix = [[None for i in range(cols)] for i in range(rows)]

    matrix[0][0] = 1

    #fill first row
    for i in range(1,cols):
        if obstacleGrid[0][i]==1:
            matrix[0][i] = 0
        else:
            matrix[0][i] = matrix[0][i-1]

    #fill first col
    for i in range(1,rows):
        if obstacleGrid[i][0]==1:
            matrix[i][0] = 0
        else:
            matrix[i][0] = matrix[i-1][0]

    # fill rest of the matrix
    for i in range(1,rows):
        for j in range(1,cols):
            if obstacleGrid[i][j]==1:
                matrix[i][j] = 0
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[rows-1][cols-1]